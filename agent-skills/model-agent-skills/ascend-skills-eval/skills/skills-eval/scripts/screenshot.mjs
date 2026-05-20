#!/usr/bin/env node
/**
 * ascend-skills-eval - 高清截图脚本
 *
 * 用法: node scripts/screenshot.mjs [html文件路径] [输出png路径]
 *
 * 特性:
 * - 2x deviceScaleFactor，输出高清图
 * - 只截 .card 元素，无多余背景
 * - 等待字体加载完成
 * - 截完自动用 open 命令打开图片
 */

import { createRequire } from 'module';
import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
const require = createRequire(import.meta.url);

function resolvePlaywright() {
  // 1) 优先使用当前项目/脚本目录可解析到的依赖
  const localCandidates = ['playwright', 'playwright-core'];
  for (const pkg of localCandidates) {
    try {
      return require(pkg);
    } catch {
      // continue
    }
  }

  // 2) 兜底：尝试从全局 npm 目录加载
  try {
    const npmGlobalRoot = execSync('npm root -g', { stdio: ['ignore', 'pipe', 'ignore'] })
      .toString()
      .trim();
    for (const pkg of localCandidates) {
      try {
        return require(path.join(npmGlobalRoot, pkg));
      } catch {
        // continue
      }
    }
  } catch {
    // ignore global resolution failures
  }

  throw new Error(
    '未找到 playwright 依赖。请先安装：\n' +
      '  npm i -D playwright\n' +
      '或\n' +
      '  npm i -D playwright-core'
  );
}

const pw = resolvePlaywright();

const args = process.argv.slice(2).filter(Boolean);
const shouldOpen = !args.includes('--no-open');
const positionalArgs = args.filter((arg) => arg !== '--no-open');

const htmlPath = positionalArgs[0] || new URL('../templates/result-card.html', import.meta.url).pathname;
const outputPath = positionalArgs[1] || new URL('../templates/result-card.png', import.meta.url).pathname;

async function launchChromium(pwApi) {
  try {
    return await pwApi.chromium.launch();
  } catch (err) {
    // 当 Playwright 自带浏览器缺失或架构不匹配时，尝试系统 Chrome/Chromium
    const browserCandidates = [
      '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      '/Applications/Chromium.app/Contents/MacOS/Chromium',
    ];
    for (const executablePath of browserCandidates) {
      if (!fs.existsSync(executablePath)) continue;
      try {
        return await pwApi.chromium.launch({ executablePath });
      } catch {
        // continue trying next candidate
      }
    }
    throw err;
  }
}

async function screenshot() {
  const browser = await launchChromium(pw);

  try {
    const context = await browser.newContext({
      viewport: { width: 920, height: 1600 },
      deviceScaleFactor: 2,
    });

    const page = await context.newPage();

    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });

    // 等待字体加载
    await page.evaluate(() => document.fonts.ready);
    // 额外等待确保渲染完成
    await page.waitForTimeout(2000);

    // 只截 .card 元素
    const card = await page.locator('.card');
    await card.screenshot({
      path: outputPath,
      type: 'png',
    });

    console.log(`截图完成: ${outputPath}`);

    // 获取图片尺寸信息
    const box = await card.boundingBox();
    console.log(`卡片尺寸: ${Math.round(box.width)}x${Math.round(box.height)}px (CSS)`);
    console.log(`输出尺寸: ${Math.round(box.width * 2)}x${Math.round(box.height * 2)}px (2x高清)`);

  } finally {
    await browser.close();
  }

  if (shouldOpen) {
    try {
      execSync(`open "${outputPath}"`, { stdio: 'ignore' });
    } catch {
      // 非 macOS 或 open 命令不可用时忽略
    }
  }
}

screenshot().catch(err => {
  console.error('截图失败:', err.message);
  if (String(err.message || '').includes("Executable doesn't exist")) {
    console.error('可尝试执行: npx playwright install chromium');
  }
  process.exit(1);
});
