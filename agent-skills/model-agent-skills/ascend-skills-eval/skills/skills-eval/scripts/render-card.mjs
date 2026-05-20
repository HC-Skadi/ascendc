#!/usr/bin/env node
import fs from "fs";
import fsp from "fs/promises";
import { createRequire } from "module";
import { execSync } from "child_process";
import path from "path";

const require = createRequire(import.meta.url);

function resolvePlaywright() {
  const pkgs = ["playwright", "playwright-core"];
  for (const pkg of pkgs) {
    try {
      return require(pkg);
    } catch {}
  }
  try {
    const root = execSync("npm root -g", { stdio: ["ignore", "pipe", "ignore"] })
      .toString()
      .trim();
    for (const pkg of pkgs) {
      try {
        return require(path.join(root, pkg));
      } catch {}
    }
  } catch {}
  throw new Error("未找到 playwright。请先执行: npm i -D playwright");
}

async function launchChromium(pw) {
  try {
    return await pw.chromium.launch();
  } catch (err) {
    const localBrowsers = [
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ];
    for (const executablePath of localBrowsers) {
      if (!fs.existsSync(executablePath)) continue;
      try {
        return await pw.chromium.launch({ executablePath });
      } catch {}
    }
    throw err;
  }
}

function parseArgs(argv) {
  const opts = { noOpen: false };
  const positional = [];
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--no-open") {
      opts.noOpen = true;
      continue;
    }
    if (["--data", "--template", "--png", "--html"].includes(arg)) {
      const v = argv[i + 1];
      if (!v || v.startsWith("--")) throw new Error(`${arg} 缺少参数值`);
      opts[arg.slice(2)] = v;
      i += 1;
      continue;
    }
    if (arg.startsWith("--")) throw new Error(`未知参数: ${arg}`);
    positional.push(arg);
  }
  if (!opts.data && positional[0]) opts.data = positional[0];
  return opts;
}

function n(value, fallback = 0) {
  const num = Number(value);
  return Number.isFinite(num) ? num : fallback;
}

function buildFields(raw) {
  const fields = { ...(raw.fields || {}) };
  for (const [k, v] of Object.entries(raw)) {
    if (k !== "fields" && k !== "dims") fields[k] = v;
  }
  const before = n(fields["score-before"]);
  const after = n(fields["score-after"]);
  if (fields["score-delta"] === undefined) {
    const delta = after - before;
    fields["score-delta"] = `${delta >= 0 ? "+" : ""}${delta}`;
  }
  if (!fields.date) {
    const d = new Date();
    fields.date = `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, "0")}.${String(
      d.getDate()
    ).padStart(2, "0")}`;
  }
  return fields;
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (!opts.data) throw new Error("请提供 --data <json文件>");

  const scriptDir = path.dirname(new URL(import.meta.url).pathname);
  const templatePath = path.resolve(opts.template || path.join(scriptDir, "../templates/result-card.html"));
  const pngPath = path.resolve(opts.png || path.join(scriptDir, "../templates/result-card.png"));
  const htmlPath = path.resolve(opts.html || path.join(scriptDir, "../templates/result-card.rendered.html"));
  const dataPath = path.resolve(opts.data);

  const raw = JSON.parse(await fsp.readFile(dataPath, "utf-8"));
  const fields = buildFields(raw);
  const dims = Array.isArray(raw.dims) ? raw.dims : [];

  const pw = resolvePlaywright();
  const browser = await launchChromium(pw);
  try {
    const context = await browser.newContext({
      viewport: { width: 920, height: 1600 },
      deviceScaleFactor: 2,
    });
    const page = await context.newPage();
    await page.goto(`file://${templatePath}`, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(600);

    await page.evaluate(
      ({ fieldsInPage, dimsInPage }) => {
        const fill = (name, value) => {
          document.querySelectorAll(`[data-field="${name}"]`).forEach((el) => {
            el.textContent = String(value);
          });
        };
        Object.entries(fieldsInPage).forEach(([k, v]) => {
          if (v !== undefined && v !== null) fill(k, v);
        });

        const before = Number(fieldsInPage["score-before"] ?? 0);
        const after = Number(fieldsInPage["score-after"] ?? 0);
        const heroStrong = document.querySelectorAll(".hero-journey strong");
        if (heroStrong.length >= 2) heroStrong[1].textContent = String(after);

        const ring = document.querySelector(".ring-progress");
        if (ring) {
          const score = Math.max(0, Math.min(100, after));
          const c = 2 * Math.PI * 85;
          ring.setAttribute("stroke-dasharray", String(c));
          ring.setAttribute("stroke-dashoffset", String(c * (1 - score / 100)));
        }

        const cells = document.querySelectorAll(".dims-grid .dim-cell");
        dimsInPage.slice(0, cells.length).forEach((d, idx) => {
          const cell = cells[idx];
          const b = Number(d.before ?? 0);
          const a = Number(d.after ?? 0);
          const delta = a - b;

          const name = cell.querySelector(".dim-name");
          const oldScore = cell.querySelector(".dim-old-score");
          const score = cell.querySelector(".dim-score");
          const arrow = cell.querySelector(".dim-arrow");

          if (name) name.textContent = String(d.name ?? "");
          if (oldScore) oldScore.textContent = String(b);
          if (score) score.textContent = String(a);
          if (arrow) {
            arrow.textContent = `${delta >= 0 ? "+" : ""}${delta}`;
            arrow.classList.remove("up-big", "up-mid", "up-small");
            if (delta >= 3) arrow.classList.add("up-big");
            else if (delta >= 2) arrow.classList.add("up-mid");
            else arrow.classList.add("up-small");
          }

          cell.classList.remove("hot", "warm");
          if (delta >= 3) cell.classList.add("hot");
          else if (delta >= 2) cell.classList.add("warm");
        });
      },
      { fieldsInPage: fields, dimsInPage: dims }
    );

    await fsp.writeFile(htmlPath, await page.content(), "utf-8");
    await page.locator(".card").screenshot({ path: pngPath, type: "png" });
    console.log(`渲染完成: ${pngPath}`);
    console.log(`已输出HTML: ${htmlPath}`);
  } finally {
    await browser.close();
  }

  if (!opts.noOpen) {
    try {
      execSync(`open "${pngPath}"`, { stdio: "ignore" });
    } catch {}
  }
}

main().catch((err) => {
  console.error("渲染失败:", err.message);
  if (String(err.message || "").includes("Executable doesn't exist")) {
    console.error("可尝试执行: npx playwright install chromium");
  }
  process.exit(1);
});
