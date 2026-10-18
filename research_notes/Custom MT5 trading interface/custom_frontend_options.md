# Custom TradingView-like Frontend on MetaTrader 5 Data (Windows, solo trader)

Research date: 2026-10-18. Method note: tradingview.com and its regional subdomains could not be fetched directly from this environment (DNS failure). TradingView terms below come from search-engine extracts of TradingView's own docs (in./ar./my.tradingview.com charting-library-docs), not a full page read. GitHub stats come from the GitHub search API on 2026-10-18 ("updated" = repo updated_at timestamp).

## TradingView libraries: Lightweight Charts vs Advanced Charts vs Trading Platform (features, licensing, eligibility)

### Takeaway
For a private, single-user desktop tool, Lightweight Charts (Apache 2.0) is the only TradingView library you can legitimately use. TradingView's own FAQ says Advanced Charts and Trading Platform are not licensed for personal, hobby, study or testing use, only for public web projects. Lightweight Charts has no built-in drawing tools or indicators, but v5 added multi-pane support and a plugin/primitive API, and community packages fill the gaps.

### Cited Findings
**Lightweight Charts (open source)**
- Repo tradingview/lightweight-charts: about 17.6k stars, 2.66k forks, 125 open issues, Apache-2.0, TypeScript, HTML5 canvas, updated 2026-10-18 — [GitHub](https://github.com/tradingview/lightweight-charts)
- Attribution requirement: "This license requires specifying TradingView as the product creator." You must include the NOTICE file's attribution notice and a link to tradingview.com on a page of your site/app that users can reach. The `attributionLogo` chart option is suggested as a way to satisfy the link requirement — [GitHub README](https://github.com/tradingview/lightweight-charts)
- Self-described as "one of the smallest and fastest financial HTML5 charts". Ships ES module and standalone IIFE builds, a plugin catalog, and two Agent Skills for AI coding assistants — [GitHub README](https://github.com/tradingview/lightweight-charts)
- v5 release: multi-pane support ("one of our most requested features"), watermark and up/down marker plugins, modular series markers, Pane Primitives for attaching plugins to panes, and a base bundle of 35 kB (16% smaller) — [TradingView blog, v5](https://www.tradingview.com/blog/en/tradingview-lightweight-charts-version-5-50837)
- The docs index lists version 5.2.1, which includes an accessibility plugin — [Algolia docsearch index of LWC docs](https://docsearch.algolia.com/mcp/docs/repo/tradingview/lightweight-charts)
- Drawing tools are not built in. Per the plugin docs, primitives are the route for "custom visualizations, drawing tools, or annotations" — [Algolia docsearch index of LWC docs](https://docsearch.algolia.com/mcp/docs/repo/tradingview/lightweight-charts)
- Community add-ons:
  - lightweight-charts-drawing v0.1.1 claims 68 drawing tools for LWC v5 (lines, channels, Fibonacci, shapes). Maintenance status was not verified — [GitHub releases](https://github.com/deepentropy/lightweight-charts-drawing/releases)
  - deepentropy/lightweight-charts-indicators claims 1,713 indicators: 117 standard, 1,551 community ports (described as Pine Script ports) and 45 candlestick patterns, with a renderer for plots, drawings and tables. 310 stars, updated 2026-10-18 — [GitHub](https://github.com/deepentropy/lightweight-charts-indicators)

**Advanced Charts (formerly "Charting Library")**
- Free only if "the TradingView attribution remains visible and the implementation environment is public (not for private use or behind a paywall)" — [TradingView Advanced Charts docs intro](https://in.tradingview.com/charting-library-docs/latest/introduction/)
- FAQ: "At this time, we do not provide the Advanced Charts and the Trading Platform libraries for personal use, hobbies, studies, or testing. The licenses can be provided only to companies and/or individuals for use in public web projects and/or applications." The same FAQ points personal projects to Lightweight Charts under Apache 2.0 — [TradingView FAQ](https://ar.tradingview.com/charting-library-docs/latest/resources/Frequently-Asked-Questions)
- Access is through an application form reviewed by TradingView. A secondary source says the license covers public-facing sites and apps, not internal tools — [Dashdevs](https://dashdevs.com/blog/tradingview-api-integration/) (secondary)
- Contains no market data; you supply your own datafeed. Pine Script, Alerts, Strategy Tester and Bar Replay are not supported because the library is client-side — [TradingView product comparison](https://in.tradingview.com/charting-library-docs/latest/product-comparison/)
- 107 built-in studies, per a third-party comparison — [LuxAlgo compare](https://www.luxalgo.com/vela/compare/) (secondary, vendor)
- Watermark is required unless enterprise removal is negotiated — [LuxAlgo compare](https://www.luxalgo.com/vela/compare.md) (secondary)
- Conflict: older Kite Connect forum posts suggest users downloaded the free library for personal use with their own broker data — [kite.trade forum](https://kite.trade/forum/discussion/comment/9540). These are informal and older, and they contradict TradingView's current FAQ.

**Trading Platform**
- "All features of Advanced Charts plus a comprehensive suite of trading capabilities" — [TradingView product comparison](https://in.tradingview.com/charting-library-docs/latest/product-comparison/)
- A vendor describes it as the "full terminal experience with order management integration, designed primarily for brokers connecting a live OMS" — [LightningChart blog](https://lightningchart.com/?p=93011) (competitor, secondary)
- Same eligibility restriction as Advanced Charts (no personal use) — [TradingView FAQ](https://ar.tradingview.com/charting-library-docs/latest/resources/Frequently-Asked-Questions)

**Related caveat**
- TradingView's own platform data and charts are "licensed for exclusive display-only use… strictly limited to personal or internal business purposes." This is a policy on TradingView-platform content, not on the libraries, but it matters if anyone considers scraping TradingView data into an automated system — [TradingView policies](https://in.tradingview.com/policies)

### Inferences
- A private desktop tool for one trader on his own Windows PC is "private use", so it falls outside the Advanced Charts and Trading Platform terms. Lightweight Charts plus plugins is the realistic TradingView-family choice, as long as the attribution link/logo stays visible.
- A practical feature stack for "TradingView feel" is LWC v5 panes for oscillators, primitives for drawings and SL/TP lines, and price lines for positions. Indicators can come from community packages or from Python-side computation.

### Gaps
- Could not load tradingview.com directly to confirm the exact current wording of the application form, or whether the 2026 terms changed after the indexed docs.
- A full Advanced Charts drawing-tool count and the Trading Platform broker-API and order-panel details were not retrieved.
- LWC GitHub Releases section appeared empty on fetch; the 5.2.1 version is from the docs index only.

## Alternatives: KLineChart, Highcharts Stock, ECharts, Plotly, lightweight-charts-python, SciChart

### Takeaway
KLineChart is the strongest free alternative if built-in drawing tools and indicators matter more than the TradingView look. lightweight-charts-python is the fastest Python-only route. Highcharts Stock and SciChart are free only for non-commercial use, and SciChart's free tier is watermarked. ECharts and Plotly are general-purpose libraries and less trading-native.

### Cited Findings
- **KLineChart** (klinecharts/KLineChart): 4.25k stars, 1.01k forks, TypeScript, canvas, zero dependencies, mobile support, updated 2026-10-18 — [GitHub](https://github.com/klinecharts/KLineChart)
  - Apache License 2.0, with built-in indicators and line-drawing models — [unpkg README klinecharts@10.0.1](https://unpkg.com/klinecharts@10.0.1/README.md)
  - KLineChart Pro: an out-of-the-box financial chart built on KLineChart, Apache-2.0 — [jsDelivr README](https://cdn.jsdelivr.net/npm/@klinecharts/pro@0.1.1/README.md); [Yarn](https://classic.yarnpkg.com/en/package/@klinecharts/pro)
- **lightweight-charts-python** (louisnw01): Python framework for TradingView LWC, real-time bar and tick updates. 2.16k stars, 443 forks, 122 open issues, updated 2026-10-14 — [GitHub](https://github.com/louisnw01/lightweight-charts-python); [docs index](https://docsearch.algolia.com/mcp/docs/repo/louisnw01/lightweight-charts-python)
- **Highcharts (incl. Stock)**: free for development/testing and for non-profit, personal website or school projects. Commercial use requires a paid license — [G2](https://www.g2.com/products/chart-js/pricing) (third-party; verify on highcharts.com)
- **SciChart.js**: the free Community License covers "personal use, non-commercial use, educational use and limited-time commercial evaluations". It is fully featured but shows a watermark; removing it needs a commercial license — [SciChart docs](https://www.scichart.com/documentation/js/v4/user-manual/licensing-scichart-js/getting-started-for-free/)
  - The 2026 pricing sheet aims the free tier at personal hobbies and open-source projects, and lists a startup discount (<$1M revenue, <5 devs) — [SciChart pricing infographic](https://www.scichart.com/wp-content/uploads/2026/03/scichart-pricing-infographic.pdf)
- **Apache ECharts**: Apache-2.0 — [package.json](https://apache.googlesource.com/echarts/+/refs/heads/master/package.json); [licenses.dev](https://licenses.dev/npm/echarts/5.5.1)
  - Canvas performance degrades at 1M+ points per a competitor benchmark — [LightningChart](https://lightningchart.com/?p=92104) (vendor; treat with caution)
- **Plotly.js**: MIT (per vendor comparison table) and about 2x slower than ECharts at 1M points in the same vendor benchmark — [LightningChart](https://lightningchart.com/?p=92104) (secondary)

### Inferences
- For a personal tool: KLineChart and LWC are both permissively licensed. Highcharts and SciChart are allowed for personal non-commercial use but carry license risk if the tool is ever shared or sold.
- Trading candles rarely need millions of points on screen, so raw throughput matters less than drawing UX, crosshair and pan feel. LWC and KLineChart are purpose-built for that.

### Gaps
- No primary-source confirmation of Plotly.js license and candlestick/real-time performance (known to be MIT from general knowledge, not cited here).
- Highcharts Stock non-commercial terms not read from highcharts.com directly.
- KLineChart's exact drawing-tool count not retrieved.

## Desktop framework options: Electron, Tauri, PyQt/PySide, local web app (FastAPI + browser)

### Takeaway
Since the MT5 Python package is Windows-only and poll-based, the backend will be Python on Windows whatever the shell. The lowest-effort path is FastAPI with a WebSocket, a React/LWC frontend, and an Edge/Chrome app-mode window or PyInstaller exe; CheapTrader ships exactly this. Tauri 2 is the lighter "real desktop app" choice, and Electron is the most mature but heaviest.

### Cited Findings
- Tauri uses the OS WebView (WebView2 on Windows) with a Rust backend; Electron bundles Chromium and Node.js — [Reintech](https://reintech.io/blog/tauri-vs-electron-rust-desktop-apps); [pkgpulse](https://www.pkgpulse.com/guides/electron-vs-tauri-2026)
- Bundle size figures conflict across blogs: 8.6 MB vs 244 MB installer; under 10 MB vs 80–150 MB; about 3 MB vs about 96 MB — [dev.to 2026 guide](https://dev.to/royce_fabbd83cb268312e928/tauri-vs-electron-vs-neutralino-2026-javascript-desktop-app-decision-guide-2kaf); [digitalapplied](https://www.digitalapplied.com/blog/desktop-apps-web-stack-tauri-electron-deno-wails-2026); [noqta](https://noqta.tn/en/blog/tauri-2-desktop-apps-rust-web-technologies-2026)
- Memory: 172 MB (Tauri) vs 409 MB (Electron) with six windows in one benchmark; roughly half the RAM in another — [pkgpulse](https://www.pkgpulse.com/guides/electron-vs-tauri-2026); [OpenReplay](https://blog.openreplay.com/comparing-electron-tauri-desktop-applications/)
- WebView2 is preinstalled on Windows 10/11. Tauri's trade-off is differing WebView bug surfaces across OSes and owning Rust native commands; Electron has the most mature ecosystem and identical rendering everywhere — [digitalapplied](https://www.digitalapplied.com/blog/desktop-apps-web-stack-tauri-electron-deno-wails-2026)
- Real example, local web app shell: CheapTrader runs FastAPI (REST `/api` plus WebSocket `/ws/stream`, bound to 127.0.0.1) and React + Vite + LWC v5. It ships as a PyInstaller single Windows exe that opens an Edge app-mode window, falling back to the default browser — [CheapTrader README](https://github.com/REDIN14/CheapTrader)
- Real example, Tauri shell: Better Charts uses Tauri 2 + Rust core + React/TS + LWC, and talks to an MT5 EA over local TCP — [Better Charts README](https://github.com/tomek-r/better-charts)
- MT5 Python package: Windows only, and connectors built on it poll for market data with no WebSocket — [NexusTrader docs](https://nexustrader.readthedocs.io/en/latest/exchange/bybit_tradfi.html)
  - It talks to the local terminal over Windows named-pipe IPC — [go-mt5 pkg docs](https://pkg.go.dev/github.com/mukbeast4/go-mt5)
  - `symbol_info_tick` maps to MQL5 SymbolInfoTick and `copy_ticks_from/range` to CopyTicks — [MQL5 book](https://www.mql5.com/de/book/advanced/python/python_funcs_overview)

### Inferences
- **PyQt/PySide** (e.g., QWebEngine hosting LWC, or lightweight-charts-python's Qt widget mode) keeps everything in one Python process. It suits a single developer who knows Python, but UI polish is slower than a React stack. Not separately sourced here.
- For real-time ticks, the bottleneck is the MT5 poll loop (Python) and the WebSocket fan-out, not the shell. Any of the four shells can render tick updates via LWC `series.update()`.
- Recommended progression for one developer: start as a local web app (FastAPI + browser). Wrap it in Tauri or a PyInstaller/Edge app window later only if a desktop feel is wanted.

### Gaps
- No independent, controlled Windows benchmark of Tauri vs Electron; all figures are blog or vendor numbers.
- No sourced data on maximum tick rate achievable with MT5 Python polling. The official docs say nothing about push callbacks; absence of callbacks is inferred from connector docs.
- Timestamp caveat: one MQL5 forum report says `symbol_info_tick().time` appears about 3h ahead of UTC on one demo build (likely broker server time). There was no official answer — [MQL5 forum](https://www.mql5.com/en/forum/517065)

## Reference architecture: MT5 -> Python package or EA bridge -> local WebSocket server -> chart UI; order entry, indicators, AI, n8n, MCP

### Takeaway
Two proven patterns exist in the wild:
- **(A) Python MetaTrader5 package** behind FastAPI REST + WebSocket, with feed, reads and orders each in a separate process (CheapTrader).
- **(B) MQL5 EA bridge** pushing data over local TCP to the app, with safety layers on execution (Better Charts).

Claude can plug in through one of several existing MT5 MCP servers, and n8n can hit the same local REST API.

### Cited Findings
**Pattern A: CheapTrader**
- Uses MetaQuotes' Python package (`copy_ticks_from`, `history_deals_get`). Live feed, reads and order placement run in separate processes so a slow terminal call doesn't stall the stream; the server process makes no MT5 calls — [CheapTrader](https://github.com/REDIN14/CheapTrader)
- Other components: SQLite bar cache and a mock broker for synthetic prices. Indicators are Python `compute(df, params)` functions run in a sandbox with time and memory limits — [CheapTrader](https://github.com/REDIN14/CheapTrader)
- Orders are disabled by default. The fetched README text also says the checked-in `backend/.env` sets `CT_ALLOW_LIVE_ORDERS=true`; verify before running — [CheapTrader](https://github.com/REDIN14/CheapTrader)

**Pattern B: Better Charts**
- `BetterChartsBridge.mq5` EA connects on 127.0.0.1:8765 with a private token, and a companion indicator supplies tick history — [Better Charts](https://github.com/tomek-r/better-charts)
- Execution safety: account/session binding, reconciliation, durable execution journals, no automatic retries, and OrderCheck validation before sending — [Better Charts](https://github.com/tomek-r/better-charts)

**Other bridges**
- Dockerized MT5 with a Python DataBridge: WebSocket hub streaming live account data plus an RPC gateway to the MetaTrader5 library — [DeadSecure repo](https://github.com/DeadSecure/Dockerized-MetaTrader5-with-Python-DataBridge)
- psyb0t/mt5-httpapi: MT5 in a Windows VM (Docker + QEMU/KVM), driven over REST + MCP. OHLC bars come enriched with RSI/MACD/Bollinger/ADX/VWAP/Ichimoku/Order Blocks/FVGs. Multi-broker. 31 stars, updated 2026-10-17 — [GitHub](https://github.com/psyb0t/mt5-httpapi)

**MCP servers for Claude** (GitHub search, 2026-10-18)
| Repo | Stars | Updated | What it does |
|---|---|---|---|
| [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) | 831 | 2026-10-17 | MCP that lets LLMs trade via MetaTrader (Python) |
| [Qoyyuum/mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server) | 232 | 2026-10-18 | Market data, trading operations, history |
| [masdevid/mt5-quant](https://github.com/masdevid/mt5-quant) | 43 | 2026-10-17 | Rust MCP for MT5 backtesting/optimization |
| [chymian/metatrader-mcp](https://github.com/chymian/metatrader-mcp) | 27 | 2026-06-07 | EA optimization |
| [PHUICMT/mcp-mt5](https://github.com/PHUICMT/mcp-mt5) | 18 | 2026-09-27 | Compile, deploy, backtest, parse reports |
| [vincentwongso/mt5-trading-mcp](https://github.com/vincentwongso/mt5-trading-mcp) | 5 | 2026-08-27 | Wraps the MT5 Python lib with a consent/audit policy layer for trades |

- remomein05/mt5-mcp: a Windows-only MCP server plus a web GUI built on TradingView Lightweight Charts, with real-time telemetry, historical export and a strategy studio with equity curve — [Glama listing](https://glama.ai/mcp/servers/remomein05/mt5-mcp)

### Inferences
Proposed layering for Bijoy:

1. **MT5 terminal (Windows)** connects to a **Python bridge service**, using the MetaTrader5 package as in Pattern A. This is simplest because his EA work already lives in MQL5, and the Python API covers bars, ticks and orders.
2. Switch to an **EA socket bridge** (Pattern B) only if tick latency or push semantics become a problem.
3. The **bridge** exposes:
   - REST for history, symbols, orders and positions
   - a WebSocket for ticks, bar updates and account/position events
4. The **UI** is React + LWC v5 with panes, drawing primitives, and SL/TP price lines dragged to modify orders.
5. **Order entry** lives only in the bridge's order process, gated by:
   - an env flag (live off by default)
   - max-risk, spread and SL-required checks that mirror the EA rules in `.claude/rules/code-standards.md`
6. **Indicators** are computed in Python (pandas) on the bridge, so signal logic can be shared with backtests and kept identical to the Pine/MQL5 versions. The results are pushed to the UI as extra series or markers.
7. **AI analysis**: Claude Code connects through an MCP server, either an existing one (ariadng / Qoyyuum) or a thin MCP wrapper over the same local REST API. A read-only toolset by default; trades need confirmation, as in vincentwongso's consent layer.
8. **n8n** calls the local REST endpoints or receives webhooks from the bridge, for example news-time alerts or posting signals to Telegram. It should never hold direct order rights without the same risk gate.

### Gaps
- n8n-specific MT5 integrations were not researched; no sources found or cited on n8n + MT5.
- The internal architecture of remomein05/mt5-mcp (WebSocket or not) was not verified.
- Licenses and code quality of the MCP servers were not audited.

## Existing open-source projects combining MT5 with Lightweight Charts or similar web UIs

### Takeaway
A few very new projects (Oct 2026) already do "TradingView-style charts on MT5". All have 0–1 stars and are early-stage, so they are best used as reference code, not dependencies. CheapTrader (Python/FastAPI/React/LWC) is the closest match to Bijoy's stack.

### Cited Findings
| Project | Stack | Features | Stars / updated | License |
|---|---|---|---|---|
| [REDIN14/CheapTrader](https://github.com/REDIN14/CheapTrader) | Python MT5 package, FastAPI, WebSocket, React/TS/Vite, LWC v5, SQLite, PyInstaller | Drawing tools that place trades (trend line, rectangle, channel, long/short boxes); drag SL/TP; risk sizing; Python indicators; bar replay with paper account; account reports | 0 / 2026-10-05 | MIT |
| [tomek-r/better-charts](https://github.com/tomek-r/better-charts) | MQL5 EA over TCP, Tauri 2 + Rust, React/TS, LWC | Six timeframes, Bid/Ask, fixed-range volume profile (POC/VAH/VAL), order ticket (Market/Limit/Stop/StopLimit) with risk sizing | 0 / 2026-10-13, 205 commits | MIT |
| [joma-dahalan/smart-money-gold-tracker](https://github.com/joma-dahalan/smart-money-gold-tracker) | Python + LWC | XAUUSD terminal; MT5/OANDA sources, liquidity heatmaps, volume profiles, automated SMC structure mapping (self-described) | 0 / created 2026-10-13 | not checked |
| [rajmeena64/extrack](https://github.com/rajmeena64/extrack) | React, LWC, Supabase | Trading journal and analytics with MT5 sync and chart review | 0 / 2026-10-17 | not checked |
| [webclinic017/Algorithmic-Trading-MT5-TV-chart](https://github.com/webclinic017/Algorithmic-Trading-MT5-TV-chart) | Python | MT5 strategy code with LWC "tv chart" | 1 / 2024-09-13 (stale) | not checked |
| [remomein05/mt5-mcp](https://glama.ai/mcp/servers/remomein05/mt5-mcp) | MCP + web GUI with LWC | Telemetry, export, strategy studio | stars not retrieved | not checked |

More detail on the two closest matches:
- **CheapTrader**: early-stage, Windows-only, spare-time project, "Phase 3 complete". Has tests and CI. No installer code signing.
- **Better Charts**: "early release tested with a demo account". Real-money trading not validated, and some chart gestures submit modifications directly when trading is enabled. Missing: partial close, break-even, multiple charts.

Building blocks rather than full apps:
- [louisnw01/lightweight-charts-python](https://github.com/louisnw01/lightweight-charts-python): 2.16k stars
- [deepentropy/lightweight-charts-indicators](https://github.com/deepentropy/lightweight-charts-indicators): 310 stars
- [deepentropy/lightweight-charts-drawing](https://github.com/deepentropy/lightweight-charts-drawing/releases): v0.1.1

### Inferences
- No mature, widely adopted (100+ star) open-source "TradingView UI for MT5" project was found. The space is fragmented and very recent.
- CheapTrader's process-isolation design and "orders off by default" flag are worth copying. Better Charts' execution journal, reconciliation and no-auto-retry rules are worth copying for order safety.
- Realistic solo build: fork or borrow from CheapTrader's architecture, and add the deepentropy indicator/drawing packages if their quality holds up. That makes an MVP (live chart, watchlist, SL/TP drag, risk-sized orders) achievable in weeks rather than months for one developer.

### Gaps
- GitHub search may miss repos that don't use the terms "mt5" or "lightweight-charts" (e.g., ones using KLineChart or ECharts with MT5). Searches like "metatrader5 chart web dashboard" returned zero results.
- Code quality, security and license files of the 0-star projects were not audited.
- Star counts change quickly; values are as of 2026-10-18.
