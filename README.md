# Hi, I'm Hubert Yang 👋

**Senior Software Engineer · Taipei, Taiwan** — 9+ years building web products, from real-time video (WebRTC)
and payments to performance and observability. These days I build games and tools **together with AI agents**
(Claude Code, Codex) and write down what works.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hubert%20Yang-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hubert-yang-01b9a51ab/)
[![CodePen](https://img.shields.io/badge/CodePen-marshal604-000?logo=codepen&logoColor=white)](https://codepen.io/marshal604)
[![Email](https://img.shields.io/badge/Email-marshal604%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:marshal604@gmail.com)

**English** · [繁體中文](#繁體中文)

---

## 🤖 AI-built projects

### 🥭 [Mango Orchard Defense](https://github.com/marshal604/mango-orchard-defense)

A top-down pixel-art web game set in a Taiwanese mango orchard: harvest mangoes, chase off thieving Formosan
macaques, sell at a roadside stand, hire workers and defeat the Monkey King. Original game; characters are
AI-generated sprite sheets cut and aligned by a custom pipeline.
`Vite` `React` `Phaser` `TypeScript` · ▶ [gameplay video](https://github.com/marshal604/mango-orchard-defense/blob/main/docs/media/gameplay.mp4)

<img src="https://raw.githubusercontent.com/marshal604/mango-orchard-defense/main/docs/media/gameplay.gif" width="640" alt="Mango Orchard Defense gameplay">

### 🦖 Digimon Survivor (fan project, private)

A Digimon fan-made survivors-style game: raise your partner from In-Training, survive the hordes of the Digital
World and choose how it evolves, following the 1999 anime lines with 進化 / 超進化 / 究極進化 cutscenes. Every move
you learn joins a random pool that can fire two or three at once, bosses and legendary rift fights escalate up to
a final Judgment, and all 100 characters have AI-generated walk / attack / idle sprites.
`TypeScript` `Canvas` `Codex image gen` `Playwright` `ffmpeg` · code is private because of the Digimon IP.

<img src="https://raw.githubusercontent.com/marshal604/marshal604/main/assets/digimon-survivor.gif" width="640" alt="Digimon Survivor gameplay">

### 📰 [stock-news-radar](https://github.com/marshal604/stock-news-radar)

An LLM news radar built to **not hallucinate**: multi-source polling (SEC EDGAR, Finviz, Google News), a primary
model cross-checked by a different auditor model, verbatim-quote oracles, keyword-vs-LLM differential checks,
numeric guardrails and a golden-set regression suite, posting tiered alerts with Chinese summaries to Discord.
`Python` `Claude` `GitHub Actions` · 129 tests

<img src="https://raw.githubusercontent.com/marshal604/marshal604/main/assets/stock-news-radar-alert.png" width="640" alt="Discord alert from stock-news-radar">

## 🧰 Open source & earlier work

- [**asana-style-extension**](https://github.com/marshal604/asana-style-extension) — Chrome extension for Asana, still in use · [Chrome Web Store](https://chromewebstore.google.com/detail/asana-helper/plhefljdadpkcldpmlaihiaeolncaghj)
- [**resume-generator**](https://github.com/marshal604/resume-generator) — the resume template generator I used early in my career

## 💼 Experience

| Role | Company | Period |
|---|---|---|
| Sr. Software Engineer | AmazingTalker | 2021 – 2026 |
| Frontend Engineer | ViewSonic | 2020 – 2021 |
| Software Engineer | Genie Network | 2018 – 2020 |
| Software Engineer | SunNet Tech | 2016 – 2018 |

Selected impact at AmazingTalker:

- Built an internal **AI-assisted debugging workflow** (codebase context + user logs + product metrics) that cut recurring frontend/RTC bug analysis from hours to minutes
- Unified TRTC and Amazon Chime into one **RTC adapter layer**, simplifying BytePlus and later Electron support
- **TTFB −70%** (400 ms → 120 ms) on a Lambda@Edge caching flow; **CI/CD −62%** (18 → 7 min); **bundle −25%**
- Moved **350 TB** of recordings to S3 with an SQS-based Node.js workflow; observability with OpenTelemetry/Grafana and New Relic
- Consolidated 30+ payment components (Stripe, PayPal, TapPay, Alipay, dLocal …) into 5 reusable modules
- Regular tech talks to 30+ engineers on WebRTC, micro-frontends, XSS prevention and GraphQL caching

**Stack:** TypeScript · React · Vue · Angular · Node.js · Electron · WebRTC · AWS · GraphQL · Phaser · Python

---

## 繁體中文

**資深軟體工程師 · 台北** — 9 年以上 Web 產品經驗，做過即時影音（WebRTC）、金流、效能優化與可觀測性。
最近專注在 **和 AI agent 一起開發**（Claude Code、Codex），用它做遊戲和工具，並把有效的做法整理下來。

**AI 作品**

- 🥭 **[芒果園保衛戰](https://github.com/marshal604/mango-orchard-defense)**：台灣芒果園主題的像素風網頁遊戲，採芒果、趕獼猴、擺攤、打倒猴王。原創遊戲，角色是 AI 生成的 sprite sheet，經自製產線切格對齊。
- 🦖 **數碼倖存者（同人作品，私人 repo）**：數碼寶貝同人割草遊戲。從幼年期培育夥伴，在數碼世界的怪潮中存活，照 1999 年動畫路線選擇進化，配上進化／超進化／究極進化演出；學會的招式會隨機施放、還能連擊，一路打 Boss、闖數碼裂縫直到最終審判，100 隻角色都有 AI 生成的走路、攻擊、待機動畫。
- 📰 **[stock-news-radar](https://github.com/marshal604/stock-news-radar)**：設計成「不會亂講話」的 LLM 新聞雷達：雙模型交叉驗證、引用必須逐字對得上原文、關鍵字與 LLM 雙路比對、數字防呆與回歸測試集，分級推送中文摘要到 Discord。

**經歷**：AmazingTalker 資深軟體工程師（2021–2026）· ViewSonic 前端工程師 · Genie Network 軟體工程師 · SunNet Tech 軟體工程師。
**學歷**：國立高雄第一科技大學 電腦與通訊工程系（2011–2015）
