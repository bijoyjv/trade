# MQL5 Platform and In-Terminal UI Customization (MetaTrader 5)

> Method note (2026-10-18): direct fetches of metatrader5.com and mql5.com were blocked by this session's egress proxy (WebFetch DNS failure; curl CONNECT 403). All findings below come from web-search result excerpts of the official pages (mql5.com docs/book/forum, metatrader5.com help and release notes). Items drawn only from prior knowledge are kept out of "Cited Findings" and flagged in "Inferences" or "Gaps". The report writer should treat exact wording of the metatrader5.com MQL5 page as partially verified.

## What does the metatrader5.com MQL5 page say? (language, program types, MetaEditor, Tester, Market/Freelance/Signals/VPS)

### Takeaway
The official page ("Development of applications in MetaQuotes Language 5 (MQL5)") positions MQL5 as MT5's built-in, C++-like, object-oriented language for trading robots (EAs), custom indicators, scripts and libraries, developed in MetaEditor (edit/debug/compile, plus a Wizard), tested in the Strategy Tester, and monetized/sourced via Market and Freelance. Services are a fifth program type documented in the MQL5 reference/book.

### Cited Findings
**The page itself**
- Page title: "Development of applications in MetaQuotes Language 5 (MQL5)"; describes MQL5 as the language for building trading robots, custom indicators, scripts and libraries for automating trading strategies — [metatrader5.com MQL5 page](https://www.metatrader5.com/en/automated-trading/mql5)
- Language claims on the page: "object-oriented architecture, the highest calculation speed, C++-like syntax" — [metatrader5.com MQL5 page](https://www.metatrader5.com/en/automated-trading/mql5)
- MetaEditor handles code editing, debugging and compiling; an MQL5 Wizard lets beginners generate a basic robot — [metatrader5.com MQL5 page](https://www.metatrader5.com/en/automated-trading/mql5)
- Expert Advisors are the trading robots; custom indicators have no access to trading functions; scripts can perform trading operations — [metatrader5.com MQL5 page](https://www.metatrader5.com/en/automated-trading/mql5)
- Parent section "Algorithmic (automated) trading in MetaTrader 5" groups MQL5, Strategy Tester, etc. — [metatrader5.com automated trading](https://www.metatrader5.com/en/automated-trading)
- MQL5.community describes MQL5 as the built-in strategy language for robots, indicators, scripts and function libraries — [mql5.com](https://www.mql5.com/en)

**Program types (MQL5 reference / book)**
- Expert Advisor: chart-attached automated system responding to init, new tick, timer events; can send trades; stored in `MQL5\Experts` — [MQL5 Reference, Language Basics](https://www.mql5.com/en/docs/mql5_guide)
- Custom indicator: cannot trade itself, can be called by other programs; `MQL5\Indicators` — [MQL5 Reference](https://www.mql5.com/en/docs/mql5_guide)
- Script: runs once, requires `OnStart`; `MQL5\Scripts` — [MQL5 Reference](https://www.mql5.com/en/docs/mql5_guide)
- Service: not attached to any chart, uses `OnStart`, designed for long cyclic background actions; `MQL5\Services` — [MQL5 Reference](https://www.mql5.com/en/docs/mql5_guide)
- Library: a set of custom functions — [MQL5 Reference](https://www.mql5.com/en/docs/mql5_guide); book chapter "Designing MQL programs of various types" covers lifecycle and features by program type — [MQL5 book](https://www.mql5.com/ja/book/applications/runtime/runtime_features_by_progtype)
- Indicators run in one common thread shared by all indicators and charts on the same symbol; EAs and scripts each run in their own thread — [WebRequest docs](https://www.mql5.com/en/docs/network/webrequest)

**MetaEditor**
- MetaEditor help: where EAs and custom indicators are written; syntax highlighting, auto-substitution, project templates — [MetaEditor Help](https://www.metatrader5.com/en/metaeditor/help)
- Build 5640 (20 Feb 2026) added Markdown support in MetaEditor and dark-theme improvements across terminal, MetaEditor and Strategy Tester — [Release notes build 5640](https://www.metatrader5.com/en/releasenotes/terminal/2430)
- MetaQuotes publishes a free book "MQL5 Programming for Traders" — [MQL5 book](https://www.mql5.com/en/book); [MetaQuotes news](https://www.metaquotes.net/en/metatrader5/news/5426)

**Strategy Tester / optimization**
- Strategy Tester page describes optimizing on one data segment and confirming on another (forward testing) and real-tick testing — [Strategy Tester](https://www.metatrader5.com/en/automated-trading/strategy-tester)
- Genetic optimization auto-enables when total optimization steps exceed 100 million; cloud's full power is used only for complete (slow) optimization; genetic runs use only one access point's agents; 64-bit required — [MQL5 Cloud Network help](https://www.metatrader5.com/en/terminal/help/mql5cloud/mql5cloud_use)
- MQL5 Cloud Network agents are paid; requires at least USD 1 on the MQL5.community account; final cost cannot be calculated in advance; own remote machines join via the MetaTester utility — [MQL5 Cloud Network help](https://www.metatrader5.com/en/terminal/help/mql5cloud/mql5cloud_use)
- Vendor figure (July 2024 forum post): 16+ billion tasks, ~50,000 agents (unverified vendor claim) — [MQL5 forum](https://www.mql5.com/en/forum/13542/54132907)

**Market / Freelance / Signals / VPS**
- Market: developers sell finished apps; Freelance: traders order custom MQL5 apps — [MetaQuotes services](https://www.metaquotes.net/en/services)
- Market rules (as quoted in forum/help): products must not call any DLL (including Windows system DLLs), "for security reasons"; seller must complete verified registration (ID documents, phone); minimum price USD 10; purchases non-refundable — [Market sell help](https://www.metatrader5.com/zh/terminal/help/market/market_sell.md); [MQL5 forum](https://www.mql5.com/en/forum/395215/30624024); [Market product with DLL](https://www.mql5.com/en/forum/10400/419482)
- MQL5 VPS: no DLLs allowed on the virtual terminal — [MQL5 forum](https://www.mql5.com/en/forum/441752/45018388)
- VPS migration transfers the current active environment (charts, EAs, signal) from the local terminal to the virtual one — [metatrader5.com news](https://www.metatrader5.com/en/news/2318.md)
- If the VPS subscription lapses, all hosting data is lost — [MQL5 forum](https://www.mql5.com/en/forum/166673/4839283)
- Build 4570: when a signal subscription is detected on the account, all MQL5 trading function calls are prohibited (regardless of whether copying is enabled in that terminal) — [Build 4570 release notes](https://www.metaquotes.net/en/metatrader5/news/5456)
- One signal per account/VPS (forum moderator statements, older) — [MQL5 forum](https://www.mql5.com/en/forum/220915)

### Inferences
- For Bijoy's gold EA: running an EA and a signal subscription on the same account is incompatible since build 4570.
- If he ever sells on Market or uses MQL5 VPS, any DLL-based UI or bridge must be avoided; sockets/WebRequest/files are the safe external channels.

### Gaps
- Could not read the full metatrader5.com MQL5 page text; section-by-section headings beyond the claims above are unverified (page fetch blocked).
- No official current statement found on Strategy Tester multi-threading/local agent counts.

## How far can the MT5 terminal look and feel be customized with MQL5? What cannot be changed?

### Takeaway
Customization is chart-centric: MQL5 can set every chart property/color, apply templates, draw graphical objects (including pixel-anchored buttons, edit boxes, rectangle labels, embedded charts), render arbitrary bitmaps via CCanvas/ResourceCreate, build windowed panels with the Standard Library `Controls` (CAppDialog), handle mouse/keyboard/object events, and even use DirectX and graphing libraries. It cannot restyle the terminal's own native windows (menus, toolbars, Navigator, Market Watch); terminal-wide light/dark theme is a user setting improved by MetaQuotes in 2026 builds.

### Cited Findings
**Chart properties, colors, templates**
- Chart colors (e.g., `CHART_COLOR_BACKGROUND`) are part of `ENUM_CHART_PROPERTY_INTEGER`; the MQL5 book includes a script that inverts all chart colors (XOR) — [MQL5 book, chart colors](https://www.mql5.com/de/book/applications/charts/charts_color)
- Set via `ChartSetInteger(chart_ID, CHART_COLOR_BACKGROUND, clr)` — [MQL5 forum](https://www.mql5.com/fr/forum/409882/36477261)
- Standard Library `CChart` wraps these: `ColorBackground`, `ShowOHLC`, `ShowGrid`, `ShowPriceScale`, `ApplyTemplate` (applies a named template file, returns bool) — [CChart ColorBackground](https://www.mql5.com/en/docs/standardlibrary/cchart/cchartcolorbackground); [CChart ApplyTemplate](https://www.mql5.com/en/docs/standardlibrary/cchart/cchartapplytemplate); [CChart SetInteger](https://www.mql5.com/en/docs/standardlibrary/cchart/cchartsetinteger)

**Graphical objects**
- `OBJ_BUTTON`, `OBJ_EDIT`, `OBJ_RECTANGLE_LABEL` (and labels/bitmap labels) are interface objects anchored to a chart corner in pixel coordinates, not price/time — [MQL4 object reference (same constants in MQL5)](https://docs.mql4.com/constants/objectconstants/enum_object_property)
- MQL5 has more object types than MQL4; notably `OBJ_CHART` embeds a symbol chart inside a chart — [MQL4 docs "MQL5 features"](https://docs.mql4.com/mql5_language/mql5_functions/mql5_customsymbols)
- Object functions take `ENUM_OBJECT` types (e.g., `ObjectName`) — [ObjectName](https://www.mql5.com/en/docs/objects/objectname)
- Terminal UI has a built-in objects list for managing chart objects — [Objects list help](https://www.metatrader5.com/en/terminal/help/charts_advanced/charts_objects_list.md)

**CCanvas / custom rendering**
- `ResourceCreate` builds bitmap resources at runtime from a pixel array (or loads images/sounds); the resource is shown through `OBJ_BITMAP` / `OBJ_BITMAP_LABEL` via `OBJPROP_BMPFILE` — [MQL5 book ResourceCreate](https://www.mql5.com/fr/book/advanced/resources/resources_resourcecreate); [MQL5 forum](https://www.mql5.com/en/forum/393733/29658281)
- `CCanvas::CreateBitmapLabel` creates both the chart object and its graphical resource; `Destroy` removes both; CCanvas has no move method (move by changing object position properties) — [MQL5 forum Canvas thread](https://mql5.com/en/forum/6410); [MQL5 article 10361](https://www.mql5.com/zh/articles/10361)
- CCanvas anti-aliasing: `PixelSetAA`, `LineAA`, `PolylineAA`, `PolygonAA`, `TriangleAA`, `CircleAA`; Build 1495 (Dec 2016) added Wu-algorithm `CircleWu`, `EllipseWu`, `LineWu`, `PolygonWu`, `PolylineWu`, `TriangleWu` — [Build 1495 release notes](https://www.metatrader5.com/en/releasenotes/terminal/1398); [Article "Studying the CCanvas Class: Anti-aliasing and Shadows"](https://www.mql5.com/en/articles/1612)
- Build 1495 also documented a graphics library to draw histograms, distributions and line graphs directly on price charts (CGraphic) — [Build 1495 release notes](https://www.metatrader5.com/en/releasenotes/terminal/1398)
- MQL5 supports DirectX 3D rendering on charts (DirectX tutorial: device, context, swap chain, "MetaQuotes hid most of the DirectX setup routine") — [DirectX Tutorial Part I](https://www.mql5.com/ko/articles/10425)

**Standard Library panels and dialogs**
- `#include <Controls\Dialog.mqh>`, subclass `CAppDialog`: window with caption, close and minimize buttons and a client area for child controls — [MQL5 blog](https://www.mql5.com/en/blogs/post/776908); [Article "Create Your Own Graphical Panels in MQL5"](https://www.mql5.com/en/forum/6100)
- Ready-made controls include `CLabel`, `CBmpButton`, `CButton`, `CEdit`, `CPanel`, `CPicture` (each built on chart graphic objects); no table/grid control, must be built manually — [MQL5 forum](https://www.mql5.com/en/forum/158433)
- Known issues: panels can break on minimize/timeframe change/drag without careful lifecycle and event routing; library historically designed for one panel per chart (second panel can receive the first's events); on-demand dialog close-event quirks — [MQL5 blog](https://www.mql5.com/en/blogs/post/776908); [Article discussion](https://www.mql5.com/en/forum/6100); [Dialog close event thread](https://www.mql5.com/en/forum/449129/47704295)
- Article "How to create a graphical panel of any complexity level" — [MQL5 forum discussion](https://mql5.com/en/forum/240684/41389798)

**Chart events**
- `OnChartEvent` receives 11 predefined types incl. `CHARTEVENT_KEYDOWN`, `CHARTEVENT_MOUSE_MOVE`, `CHARTEVENT_OBJECT_CREATE`, `CHARTEVENT_OBJECT_CLICK`, `CHARTEVENT_CHART_CHANGE` — [Types of Chart Events](https://www.mql5.com/en/docs/constants/chartconstants/enum_chartevents)
- Custom events: `EventChartCustom(chart_id, id, lparam, dparam, sparam)`; 65535 IDs from `CHARTEVENT_CUSTOM` to `CHARTEVENT_CUSTOM_LAST`; string truncated beyond 63 chars; usable for program-to-program messaging across charts — [MQL5 book custom events](https://www.mql5.com/de/book/applications/events/events_custom); [MQL4 EventChartCustom](https://docs.mql4.com/eventfunctions/eventchartcustom); [EA1 to EA2 thread](https://www.mql5.com/en/forum/170560)
- In the Strategy Tester only custom events are supported (forum statement) — [MQL5 forum](https://mql5.com/en/forum/425321)

**Custom symbols**
- `CustomSymbolCreate(name, path, origin)` creates symbols from server symbols, text files or external sources; `CustomTicksAdd`, `CustomRatesUpdate` feed history/ticks (e.g., from a remote server in real time) — [Custom Symbols](https://docs.mql4.com/mql5_language/mql5_functions/mql5_customsymbols); [MQL5 book](https://www.mql5.com/ja/book/advanced/custom_symbols/custom_symbols_create_delete); [Remote feed thread](https://www.mql5.com/en/forum/217512/5908550)
- Reported bugs: ticks not appearing despite success return; wrong decimals at digits=2 (forum, unconfirmed) — [MQL5 forum](https://www.mql5.com/en/forum/294895/9896813)

**Terminal theme (not MQL5)**
- Build 5640 (Feb 2026) improved dark theme in terminal, MetaEditor, Tester; reportedly reverted from Blend2D to GDI rendering; Build 5830 (24 Apr 2026) tuned dark mode for help, OHLC line, chart collapse buttons, tester inputs — [Build 5640](https://www.metatrader5.com/en/releasenotes/terminal/2430); [Build 5830](https://www.metatrader5.com/en/releasenotes/terminal/2437)

### Inferences
- A full custom "trading cockpit" (dark panel, buy/sell buttons, risk calculator, PnL display, custom-drawn levels/heatmaps) is feasible entirely on a chart via CAppDialog + CCanvas + OnChartEvent; a full-screen custom look is achievable by hiding chart elements (grid, OHLC, scale) and painting a CCanvas over the chart.
- Not changeable from MQL5 (prior knowledge, not verified in this session): terminal menus, toolbars, Navigator/Market Watch/Toolbox windows, native order dialog, fonts of native UI; MQL5 has no API to add menu items or dockable native windows. All MQL5 UI lives inside chart windows (or chart subwindows).
- Services have no chart, so they cannot own UI; UI must live in an EA/indicator on a chart.

### Gaps
- Full official `ENUM_OBJECT` list and `ENUM_CHART_PROPERTY_INTEGER` (e.g., `CHART_SHOW`) not retrieved.
- No official page retrieved explicitly listing what the terminal UI does NOT allow; the "not changeable" list above is inference.
- Profiles (saved workspace sets) not covered by retrieved sources.

## Which MQL5 features let an EA stream data out to, or receive commands from, an external app?

### Takeaway
Five official channels: WebRequest (HTTP/HTTPS, whitelisted URLs), Socket* functions (raw TCP/TLS, whitelisted hosts, max 128 sockets), DLL imports (two-level permission, banned on Market and MQL5 VPS), files in the shared `FILE_COMMON` folder, and named pipes via FileOpen (MQL5 as client). Plus the official Python `MetaTrader5` package that drives the terminal from outside. Network functions are unavailable in indicators and WebRequest is unavailable in the Strategy Tester.

### Cited Findings
- WebRequest: callable only from EAs and scripts; in indicators returns error 4014 "Function is not allowed for call"; URLs must be added under Tools > Options > Expert Advisors; port auto-chosen (80 http, 443 https); cannot run in the Strategy Tester — [WebRequest docs](https://www.mql5.com/en/docs/network/webrequest); [MQL5 book HTTP](https://www.mql5.com/en/book/advanced/network/network_http)
- Sockets (`SocketCreate`, `SocketConnect`, `SocketSend`, ...): EAs and scripts only (4014 in indicators); address must be on the allowed list (Tools > Options > Expert Advisors), else error 5272 `ERR_NETSOCKET_CANNOT_CONNECT`; max 128 sockets per MQL program — [SocketCreate](https://mql5.com/ko/docs/network/socketcreate); [SocketConnect](https://www.mql5.com/ko/docs/network/socketconnect); [SocketSend](https://www.mql5.com/en/docs/network/socketsend)
- Forum users report 4014 for sockets in the Strategy Tester (anecdotal, no official statement found) — [MQL5 forum](https://www.mql5.com/en/forum/349124)
- Push notifications are covered alongside sockets in the MQL5 book network chapter — [MQL5 book](https://www.mql5.com/pt/book/advanced/network/network_socket_create_connect)
- MT5-Python socket integration articles exist — [Article discussion](https://www.mql5.com/en/forum/308679/15728764); [MT5 and Python via socket](https://www.mql5.com/en/forum/331936/16291247)
- DLL imports (`#import`): two-level permission (terminal-wide default plus per-program "Allow DLL imports"); docs advise disabling for unknown EAs; DLL calls prohibited on remote tester agents (local agents only) — [MQL5 book env permissions](https://www.mql5.com/fr/book/common/environment/env_permissions); [MQL5 book DLL specifics](https://www.mql5.com/it/book/advanced/libraries/libraries_dll)
- Files: `FILE_COMMON` opens files in a folder shared by all MT5 terminals (otherwise `MQL5\Files`); readers of files rewritten by an external app need `FILE_READ|FILE_SHARE_READ` — [FileOpen docs](https://www.mql5.com/en/docs/files/FileOpen); [Java to EA thread](https://www.mql5.com/en/forum/167951/4029296)
- Named pipes: `FileOpen("\\\\.\\pipe\\name")`; call `FileFlush()`/`FileSeek()` between read/write; article "Communicating With MetaTrader 5 Using Named Pipes Without Using DLLs"; MQL cannot act as pipe server (forum) — [FileOpen docs](https://www.mql5.com/en/docs/files/FileOpen); [MQL5 forum](https://www.mql5.com/en/forum/98967/2924062)
- Python `MetaTrader5` package: functions like `copy_rates_from/_from_pos/_range` (mirror CopyRates), `order_send` taking a dict request — [MQL5 book Python](https://www.mql5.com/de/book/advanced/python/python_funcs_overview); [Python user group](https://www.mql5.com/en/forum/393357/29250623)
- Inter-program messaging inside the terminal: `EventChartCustom` — [Types of Chart Events](https://www.mql5.com/en/docs/constants/chartconstants/enum_chartevents)

### Inferences
- Recommended architecture for streaming out/receiving commands: EA (own thread) or Service runs a socket client to a local server (e.g., Python on 127.0.0.1), polling via `OnTimer`; whitelist the address. Indicators cannot do network I/O, so indicator-derived signals must be relayed through an EA/service or chart events.
- WebRequest is synchronous/blocking (prior knowledge, verify) so it is unsuitable for high-frequency streaming; sockets are better.
- Backtesting an EA that depends on external commands needs a file- or stub-based fallback since WebRequest (and likely sockets) do not work in the tester.

### Gaps
- Exact WebRequest timeout semantics, supported methods and TLS details for sockets (`SocketTlsHandshake`) not retrieved.
- No official confirmation of sockets behavior in the Strategy Tester.
- Physical path of the common folder not retrieved.

## Technical limitations relevant to a solo trader (India focus is technical only)

### Takeaway
Key constraints: Windows-native terminal; indicators are single-threaded per symbol and cannot do network I/O; DLLs are banned on Market and MQL5 VPS; signal subscriptions block MQL5 trading on that account; cloud optimization costs money and cost is not predictable; VPS data is lost if the subscription lapses.

### Cited Findings
- Indicators share one thread per symbol; network functions blocked in indicators — [WebRequest docs](https://www.mql5.com/en/docs/network/webrequest)
- DLL banned on Market and on MQL5 VPS — [Market sell help](https://www.metatrader5.com/zh/terminal/help/market/market_sell.md); [MQL5 forum](https://www.mql5.com/en/forum/441752/45018388)
- Signal subscription blocks MQL5 trading functions — [Build 4570](https://www.metaquotes.net/en/metatrader5/news/5456)
- MQL5 Cloud Network is paid, minimum USD 1 balance, cost unpredictable — [Cloud help](https://www.metatrader5.com/en/terminal/help/mql5cloud/mql5cloud_use)
- VPS lapse loses all hosting data — [MQL5 forum](https://www.mql5.com/en/forum/166673/4839283)
- Python `copy_*_range` memory growth reported in loops (forum) — [Python user group](https://www.mql5.com/en/forum/393357/29241957)
- CCanvas/CAppDialog panels need lifecycle handling to survive timeframe changes — [MQL5 blog](https://www.mql5.com/en/blogs/post/776908)

### Inferences
- With an IST-based schedule, MQL5 VPS or a Windows VPS lets the EA run through London/NY sessions while the PC is off, but DLL-free design is required for MQL5 VPS.
- The `MetaTrader5` Python package is Windows-only (prior knowledge, verify); on macOS/Linux MT5 runs under Wine.

### Gaps
- No sources retrieved on India-specific technical limits (e.g., network latency to broker servers); none found.
- Platform OS support (Windows/macOS/Linux/Web) not confirmed in this session.
