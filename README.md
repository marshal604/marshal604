# Hi, I'm Hubert Yang 👋

**Senior Software Engineer · Taipei, Taiwan** — 9+ years building web products, from real-time video (WebRTC)
and payments to performance and observability. These days I build games and tools **together with AI agents**
(Claude Code, Codex) and write down what works.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hubert%20Yang-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hubert-yang-01b9a51ab/)
[![CodePen](https://img.shields.io/badge/CodePen-marshal604-000?logo=codepen&logoColor=white)](https://codepen.io/marshal604)
[![Email](https://img.shields.io/badge/Email-marshal604%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:marshal604@gmail.com)

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
`TypeScript` `Canvas` `Codex image gen` `Playwright` `ffmpeg`

> **Why the repo is private:** Digimon and its characters, names and attacks belong to Bandai / Toei Animation /
> Akiyoshi Hongo. This is a non-commercial fan project, so I don't redistribute it publicly. Happy to walk through
> the code and the AI workflow behind it on request.

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
