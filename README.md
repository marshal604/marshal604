# Hi, I'm Hubert Yang 👋

**Senior Software Engineer · Taipei, Taiwan** — 9+ years building web products, from real-time video (WebRTC)
and payments to performance and observability. These days I build games and tools **together with AI agents**
(Claude Code, Codex) and write down what works.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hubert%20Yang-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hubert-yang-01b9a51ab/)
[![CodePen](https://img.shields.io/badge/CodePen-marshal604-000?logo=codepen&logoColor=white)](https://codepen.io/marshal604)
[![Email](https://img.shields.io/badge/Email-marshal604%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:marshal604@gmail.com)

---

## ✨ Highlights

<table>
<tr>
<td width="50%" valign="top"><img src="https://raw.githubusercontent.com/marshal604/marshal604/main/assets/digimon-survivor.gif" alt="Digimon Survivor"><br><b>Digimon Survivor</b><br><sub>Survivors-style fan game with anime evolutions and 100 AI-drawn characters</sub></td>
<td width="50%" valign="top"><a href="https://github.com/marshal604/ai-novel-studio"><img src="https://raw.githubusercontent.com/marshal604/ai-novel-studio/main/office/docs/media/office-timelapse.gif" alt="AI Novel Studio"></a><br><a href="https://github.com/marshal604/ai-novel-studio"><b>AI Novel Studio</b></a><br><sub>Four AI agents write a novel together, replayed as a pixel-art office</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://github.com/marshal604/mango-orchard-defense"><img src="https://raw.githubusercontent.com/marshal604/mango-orchard-defense/main/docs/media/gameplay.gif" alt="Mango Orchard Defense"></a><br><a href="https://github.com/marshal604/mango-orchard-defense"><b>Mango Orchard Defense</b></a><br><sub>Original pixel-art game in a Taiwanese mango orchard</sub></td>
<td width="50%" valign="top"><a href="https://github.com/marshal604/ai-shorts"><img src="https://raw.githubusercontent.com/marshal604/ai-shorts/main/docs/media/reel.gif" alt="AI Shorts"></a><br><a href="https://github.com/marshal604/ai-shorts"><b>AI Shorts</b></a><br><sub>One long recording in, ready-to-post vertical shorts out</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://github.com/marshal604/at-badminton-landing"><img src="https://raw.githubusercontent.com/marshal604/at-badminton-landing/main/docs/media/event-page.gif" alt="AT Badminton Cup"></a><br><a href="https://github.com/marshal604/at-badminton-landing"><b>AT Badminton Cup</b></a><br><sub>Promo and live-scoring site for my badminton club's tournament</sub></td>
<td width="50%" valign="top"><a href="https://github.com/marshal604/stock-news-radar"><img src="https://raw.githubusercontent.com/marshal604/marshal604/main/assets/stock-news-radar-alert.png" alt="stock-news-radar"></a><br><a href="https://github.com/marshal604/stock-news-radar"><b>stock-news-radar</b></a><br><sub>LLM news alerts that are cross-checked before they are posted</sub></td>
</tr>
</table>

## 🤖 AI-built projects

### 🦖 Digimon Survivor (fan project, private)

A Digimon fan-made survivors-style game: raise your partner from In-Training, survive the hordes of the Digital
World and choose how it evolves, following the 1999 anime lines with 進化 / 超進化 / 究極進化 cutscenes. Every move
you learn joins a random pool that can fire two or three at once, bosses and legendary rift fights escalate up to
a final Judgment, and all 100 characters have AI-generated walk / attack / idle sprites.
`TypeScript` `Canvas` `Codex image gen` `Playwright` `ffmpeg`

<sub>Code is private: Digimon names, characters and attacks belong to Bandai / Toei Animation / Akiyoshi Hongo, so this non-commercial fan project isn't redistributed. Happy to walk through it on request.</sub>

### 🏢 [AI Novel Studio](https://github.com/marshal604/ai-novel-studio)

A four-role AI editorial office (editor-in-chief, writer, worldbuilder, critic) that writes novels inside Claude Code,
and a pixel-art office that replays the team at work: kickoff meetings, drafting, parallel reviews, revisions and
sign-off. I measured the first version's runs and redesigned the workflow with Codex as a reviewer: one-shot
subagents, structured JSON reviews and a small CLI for the bookkeeping cut cost per chapter by 43% ($1.54 → $0.87).
`Claude Code` `Node.js` `Phaser` `TypeScript`

### 🥭 [Mango Orchard Defense](https://github.com/marshal604/mango-orchard-defense)

A top-down pixel-art web game set in a Taiwanese mango orchard: harvest mangoes, chase off thieving Formosan
macaques, sell at a roadside stand, hire workers and defeat the Monkey King. Original game; characters are
AI-generated sprite sheets cut and aligned by a custom pipeline.
`Vite` `React` `Phaser` `TypeScript`

### ✂️ [AI Shorts](https://github.com/marshal604/ai-shorts)

A CLI that turns one long, unedited trading-analysis screen recording into several ready-to-post 9:16 shorts, one
per trade: spoken anchor phrases locate each trade, a category (vocabulary, story skeleton, music) drives the plan,
an LLM writes the caption cards and ffmpeg renders the result. The engine knows no topic; categories hold all the
domain knowledge.
`TypeScript` `ffmpeg` `whisper.cpp` `Claude`

### 📰 [stock-news-radar](https://github.com/marshal604/stock-news-radar)

An LLM news radar built to **not hallucinate**: multi-source polling (SEC EDGAR, Finviz, Google News), a primary
model cross-checked by a different auditor model, verbatim-quote oracles, keyword-vs-LLM differential checks,
numeric guardrails and a golden-set regression suite, posting tiered alerts with Chinese summaries to Discord.
`Python` `Claude` `GitHub Actions` · 129 tests

## 🧰 Other projects

- [**AT Badminton Cup**](https://github.com/marshal604/at-badminton-landing) — promo and live-scoring site for my badminton club's tournament (round-robin schedule, live standings, Google Sheets scoring) · [live site](https://marshal604.github.io/at-badminton-landing/2026-02-07)
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
