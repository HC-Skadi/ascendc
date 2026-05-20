#!/usr/bin/env node
/**
 * Render result card from JSON data.
 *
 * Usage:
 *   node scripts/render-card.mjs --data ./templates/result-card.sample.json
 *   node scripts/render-card.mjs --data ./data.json --png ./out.png --html ./out.html --no-open
 *
 * JSON format (top-level keys are allowed):
 * {
 *   "skill-name": "ascend-npu-verifier",
 *   "skill-id": "ascend-npu-verifier",
 *   "score-before": 72,
 *   "score-after": 87,
 *   "improve-1": "...",
 *   "improve-2": "...",
 *   "improve-3": "...",
 *   "dims": [
 *     {"name":"元数据","before":6,"after":8},
 *     {"name":"工作流","before":5,"after":8}
 *   ],
 *   "fields": {
 *     "top1-story": "..."
 *   }
 * }
 */

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
    } catch {
      // try next
    }
  }

  try {
    const npmGlobalRoot = execSync("npm root -g", {
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
    for (const pkg of pkgs) {
      try {
        return require(path.join(npmGlobalRoot, pkg));
      } catch {
        // try next
      }
    }
  } catch {
    // ignore
  }

  throw new Error(
    "未找到 playwright 依赖。请先安装：\n" +
      "  npm i -D playwright\n" +
      "或\n" +
      "  npm i -D playwright-core"
  );
}

async function launchChromium(pwApi) {
  try {
    return await pwApi.chromium.launch();
  } catch (err) {
    const browserCandidates = [
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ];

    for (const executablePath of browserCandidates) {
      if (!fs.existsSync(executablePath)) continue;
      try {
        return await pwApi.chromium.launch({ executablePath });
      } catch {
        // try next
      }
    }
    throw err;
  }
}

function parseArgs(argv) {
  const options = {
    noOpen: false,
  };
  const positional = [];

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--no-open") {
      options.noOpen = true;
    } else if (arg === "--data" || arg === "--template" || arg === "--png" || arg === "--html") {
      const value = argv[i + 1];
      if (!value || value.startsWith("--")) {
        throw new Error(`参数 ${arg} 缺少值`);
      }
      options[arg.slice(2)] = value;
      i += 1;
    } else if (arg.startsWith("--")) {
      throw new Error(`未知参数: ${arg}`);
    } else {
      positional.push(arg);
    }
  }

  if (!options.data && positional.length > 0) {
    options.data = positional[0];
  }

  return options;
}

function toNumber(value, fallback = 0) {
  const n = Number(value);
  return Number.isFinite(n) ? n : fallback;
}

function pickTopBreakthroughs(dims) {
  const normalized = (Array.isArray(dims) ? dims : [])
    .map((d) => ({
      name: String(d?.name ?? ""),
      before: toNumber(d?.before, 0),
      after: toNumber(d?.after, 0),
    }))
    .filter((d) => d.name);

  const withDelta = normalized.map((d) => ({
    ...d,
    delta: d.after - d.before,
  }));

  withDelta.sort((a, b) => b.delta - a.delta);
  return withDelta.slice(0, 2);
}

function buildFields(rawData) {
  const reserved = new Set(["fields", "dims"]);
  const fields = { ...(rawData.fields || {}) };

  for (const [key, value] of Object.entries(rawData)) {
    if (!reserved.has(key)) {
      fields[key] = value;
    }
  }

  const scoreBefore = toNumber(fields["score-before"], 0);
  const scoreAfter = toNumber(fields["score-after"], 0);
  if (fields["score-delta"] === undefined) {
    fields["score-delta"] = `${scoreAfter - scoreBefore >= 0 ? "+" : ""}${scoreAfter - scoreBefore}`;
  }

  if (!fields.date) {
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, "0");
    const dd = String(now.getDate()).padStart(2, "0");
    fields.date = `${yyyy}.${mm}.${dd}`;
  }

  const top = pickTopBreakthroughs(rawData.dims);
  if (top[0]) {
    if (!fields["top1-name"]) fields["top1-name"] = top[0].name;
    if (fields["top1-from"] === undefined) fields["top1-from"] = top[0].before;
    if (fields["top1-to"] === undefined) fields["top1-to"] = top[0].after;
    if (!fields["top1-pct"]) {
      const pct = top[0].before > 0 ? Math.round((top[0].delta / top[0].before) * 100) : 100;
      fields["top1-pct"] = `${top[0].delta >= 0 ? "+" : ""}${pct}%`;
    }
  }
  if (top[1]) {
    if (!fields["top2-name"]) fields["top2-name"] = top[1].name;
    if (fields["top2-from"] === undefined) fields["top2-from"] = top[1].before;
    if (fields["top2-to"] === undefined) fields["top2-to"] = top[1].after;
    if (!fields["top2-pct"]) {
      const pct = top[1].before > 0 ? Math.round((top[1].delta / top[1].before) * 100) : 100;
      fields["top2-pct"] = `${top[1].delta >= 0 ? "+" : ""}${pct}%`;
    }
  }

  return fields;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  const scriptDir = path.dirname(new URL(import.meta.url).pathname);
  const defaultTemplatePath = path.resolve(scriptDir, "../templates/result-card.html");
  const defaultPngPath = path.resolve(scriptDir, "../templates/result-card.png");
  const defaultHtmlPath = path.resolve(scriptDir, "../templates/result-card.rendered.html");

  const templatePath = path.resolve(options.template || defaultTemplatePath);
  const dataPath = options.data ? path.resolve(options.data) : null;
  const outputPngPath = path.resolve(options.png || defaultPngPath);
  const outputHtmlPath = options.html ? path.resolve(options.html) : defaultHtmlPath;

  if (!dataPath) {
    throw new Error("缺少 --data 参数（或第一个位置参数作为 data.json）");
  }

  const jsonText = await fsp.readFile(dataPath, "utf-8");
  const rawData = JSON.parse(jsonText);
  const dims = Array.isArray(rawData.dims) ? rawData.dims : [];
  const fields = buildFields(rawData);

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
    await page.waitForTimeout(800);

    await page.evaluate(
      ({ fieldsInPage, dimsInPage }) => {
        const setTextByField = (field, value) => {
          const nodes = document.querySelectorAll(`[data-field="${field}"]`);
          nodes.forEach((node) => {
            node.textContent = String(value);
          });
        };

        Object.entries(fieldsInPage).forEach(([k, v]) => {
          if (v !== undefined && v !== null) {
            setTextByField(k, v);
          }
        });

        const scoreBefore = Number(fieldsInPage["score-before"] ?? 0);
        const scoreAfter = Number(fieldsInPage["score-after"] ?? 0);
        const scoreDelta = scoreAfter - scoreBefore;
        if (!Number.isNaN(scoreDelta)) {
          setTextByField("score-delta", `${scoreDelta >= 0 ? "+" : ""}${scoreDelta}`);
        }

        // Hero sentence second strong has no data-field in template
        const heroStrongNodes = document.querySelectorAll(".hero-journey strong");
        if (heroStrongNodes.length >= 2 && Number.isFinite(scoreAfter)) {
          heroStrongNodes[1].textContent = String(scoreAfter);
        }

        // Ring progress update based on score-after (0-100)
        const ring = document.querySelector(".ring-progress");
        if (ring && Number.isFinite(scoreAfter)) {
          const scoreClamped = Math.max(0, Math.min(100, scoreAfter));
          const circumference = 2 * Math.PI * 85; // r = 85
          ring.setAttribute("stroke-dasharray", String(circumference));
          ring.setAttribute("stroke-dashoffset", String(circumference * (1 - scoreClamped / 100)));
        }

        // Fill dimension cards
        const cells = document.querySelectorAll(".dims-grid .dim-cell");
        dimsInPage.slice(0, cells.length).forEach((dim, idx) => {
          const cell = cells[idx];
          const before = Number(dim.before ?? 0);
          const after = Number(dim.after ?? 0);
          const delta = after - before;

          const nameEl = cell.querySelector(".dim-name");
          const oldEl = cell.querySelector(".dim-old-score");
          const scoreEl = cell.querySelector(".dim-score");
          const arrowEl = cell.querySelector(".dim-arrow");

          if (nameEl) nameEl.textContent = String(dim.name ?? "");
          if (oldEl) oldEl.textContent = String(before);
          if (scoreEl) scoreEl.textContent = String(after);

          if (arrowEl) {
            arrowEl.textContent = `${delta >= 0 ? "+" : ""}${delta}`;
            arrowEl.classList.remove("up-big", "up-mid", "up-small");
            if (delta >= 3) arrowEl.classList.add("up-big");
            else if (delta >= 2) arrowEl.classList.add("up-mid");
            else arrowEl.classList.add("up-small");
          }

          cell.classList.remove("hot", "warm");
          if (delta >= 3) cell.classList.add("hot");
          else if (delta >= 2) cell.classList.add("warm");
        });
      },
      { fieldsInPage: fields, dimsInPage: dims }
    );

    const renderedHtml = await page.content();
    await fsp.writeFile(outputHtmlPath, renderedHtml, "utf-8");

    const card = page.locator(".card");
    await card.screenshot({
      path: outputPngPath,
      type: "png",
    });

    const box = await card.boundingBox();
    console.log(`渲染完成: ${outputPngPath}`);
    console.log(`已输出HTML: ${outputHtmlPath}`);
    if (box) {
      console.log(`卡片尺寸: ${Math.round(box.width)}x${Math.round(box.height)}px (CSS)`);
      console.log(`输出尺寸: ${Math.round(box.width * 2)}x${Math.round(box.height * 2)}px (2x高清)`);
    }
  } finally {
    await browser.close();
  }

  if (!options.noOpen) {
    try {
      execSync(`open "${outputPngPath}"`, { stdio: "ignore" });
    } catch {
      // ignore on non-macOS
    }
  }
}

main().catch((err) => {
  console.error("渲染失败:", err.message);
  if (String(err.message || "").includes("Executable doesn't exist")) {
    console.error("可尝试执行: npx playwright install chromium");
  }
  process.exit(1);
});
