# External Integration with MetaTrader 5 and Licensing Limits on a "Custom MT5"

Research date: 2026-10-18. Method note: this session's network policy blocked direct fetches of mql5.com, metaapi.cloud, metaquotes.net, financemagnates.com, readthedocs.io and the GitHub API. Only pypi.org could be fetched directly. Most findings below come from search-result extracts of the cited pages, not full-page reads. Items marked "(background, unverified this session)" are from prior knowledge and must be checked before use.

## 1. Official MetaTrader5 Python package

### Takeaway
The official `MetaTrader5` package (MIT, v5.0.6231, released 2026-09-27) is a Windows-only, x86-64 IPC client to a locally installed desktop terminal. It covers market data (bars, ticks, symbol info), account info, and trading (`order_send`, positions, history). It is request/response only, so "streaming" means polling. Linux/macOS use requires Wine plus an RPC bridge such as mt5linux.

### Cited Findings
- Latest version 5.0.6231, released 2026-09-27. Requires Python >=3.6,<4, with classifiers for 3.6 through 3.14. License is MIT. All published wheels are Windows x86-64 and there are no Linux/macOS wheels. — [PyPI: MetaTrader5](https://pypi.org/project/MetaTrader5/)
- The official docs list the Python Integration module. `initialize(path=...)` takes the path to `terminal64.exe`/`metatrader64.exe`. The path is optional, and if it is omitted the module tries to find the terminal itself. — [MQL5 docs: initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py); [MQL5 docs: Python Integration](https://www.mql5.com/en/docs/python_metatrader5)
- The MQL5 book maps each Python function to its MQL5 equivalent: `symbol_info_tick`→SymbolInfoTick, `copy_ticks_from`→CopyTicks, `order_send`→OrderSend. It also documents `positions_get` and `history_deals_get`. — [MQL5 book: Python functions overview](https://www.mql5.com/de/book/advanced/python/python_funcs_overview)
- `copy_ticks_from(symbol, date_from, count, flags)` takes flags such as `COPY_TICKS_ALL`. The example calls `initialize()` first and exits on failure. — [MQL5 book: Reading tick history](https://mql5.com/de/book/advanced/python/python_copyticks)
- `copy_ticks_range` returns ticks for a date range from the terminal. Forum users report it failing on multi-year ranges, and the threads have no resolution posted (forum reports, not documented limits). — [MQL5 docs](https://www.mql5.com/en/docs/python_metatrader5); [Forum 391710](https://www.mql5.com/en/forum/391710); [Forum 456556](https://www.mql5.com/en/forum/456556)
- `order_send` takes a dict request (action, symbol, volume, type, price, deviation…). A forum example pulls the price from `symbol_info_tick` and retries on requotes. — [MQL5 forum: Python user group p.39](https://www.mql5.com/en/forum/393357/29241957)
- `history_deals_get` accepts filters for symbol, ticket, position and date range (third-party wrapper docs). — [glama.ai mcp-trader API reference](https://glama.ai/mcp/servers/@Af7007/mcp-trader/blob/e59df7f2e1cf8cec8b3e72d971084f942e1d3992/docs/api_reference.md)
- The pymt5 project says the official package talks to a locally installed desktop terminal. pymt5 instead uses the MT5 Web Terminal's WebSocket protocol, which it reverse-engineered, and its `symbol_info_tick` comes from cached push data. — [pymt5 comparison doc](https://pymt5.readthedocs.io/en/latest/python_api_detailed_comparison.html)
- mt5linux runs a Windows Python plus the MetaTrader5 package under Wine and exposes it to Linux over RPyC (default TCP port 18812). — [PyPI: mt5linux](https://pypi.org/project/mt5linux); [GitHub: tiloye/mt5linux](https://github.com/tiloye/mt5linux)

### Inferences
- The package has no callback or subscription API (confirmed only indirectly, by pymt5 contrasting itself with "push" data). Real-time use means polling `symbol_info_tick` / `copy_ticks_from` in a loop. Latency is bounded by poll interval plus IPC, and you can miss ticks between polls unless you backfill with `copy_ticks_from`.
- The terminal must be installed, logged in to a broker account, and running, since the package attaches to it. "Algo Trading" must be enabled for `order_send` to work (background, unverified this session).
- Bar history depth is likely capped by the terminal's "Max bars in chart" setting (background, unverified; no source retrieved).
- pymt5 uses a reverse-engineered protocol, which likely falls under the EULA's anti-reverse-engineering clause (see section 4).

### Gaps
- The full official function list (account_info, terminal_info, symbols_get, market_book_add/get, order_check, orders_get, history_orders_get, last_error, shutdown) could not be read directly. These names are background knowledge.
- No documented polling rate limit or maximum tick count per call was found.

## 2. Bridge approaches (EA + ZeroMQ / sockets / WebSocket / named pipes / REST)

### Takeaway
The best-known bridge, Darwinex's DWX ZeroMQ Connector, was MT4-only and has been archived since 2022-02-15. Its successor, DWX Connect, supports MT4/MT5. Most other bridges are small community projects of uneven maintenance. All of them still need a running Windows terminal with an EA attached.

### Cited Findings
- DWX ZeroMQ Connector was archived and no longer maintained as of 2022-02-15. It targeted Python 3 ↔ MetaTrader 4 via ZeroMQ, and users were told to migrate to DWX Connect. — [Algolia DocSearch mirror of darwinex/dwx-zeromq-connector](https://docsearch.algolia.com/mcp/docs/repo/darwinex/dwx-zeromq-connector); [gittrend: dwx-zeromq-connector](https://gittrend.io/repo/darwinex/dwx-zeromq-connector)
- Darwinex's GitHub lists `dwxconnect` as a "fully customizable trading API" linking strategies in any language via MetaTrader 4 or 5. — [GitHub: darwinex](https://www.Github.com/darwinex)
- Community forks of the DWX ZeroMQ connector exist (e.g., artbert, "v2.0.1"). No MT5 ZeroMQ fork was confirmed. — [GitHub: artbert/dwx-zeromq-connector](https://github.com/artbert/dwx-zeromq-connector)
- Third-party REST/HTTP bridges exist (e.g., the `mt5api` PyPI package, the Docker image `liberatti/mt5bridge`, psyb0t mt5-httpapi). At least one notes the API server must run on Windows. — [PyPI: mt5api](https://pypi.org/project/mt5api/); [Docker Hub: liberatti/mt5bridge](https://hub.docker.com/r/liberatti/mt5bridge); [getclawkit: psyb0t mt5 httpapi](https://getclawkit.com/skills/official-psyb0t-mt5-httpapi)
- Many MCP servers now wrap the official Python package, e.g., MetaTrader-5-MCP-Server, mcpmt5 and a Linux/mac variant. — [glama.ai MetaTrader-5-MCP-Server](https://glama.ai/mcp/servers/@Cloudmeru/MetaTrader-5-MCP-Server/blob/e5d2c877d147ecd89468c121ec05522f000d38b2/src/mt5_mcp/server.py); [claudemarket.ai metatrader-mcp-server-mac](https://claudemarket.ai/mcp/pongsakorn-onsri/metatrader-mcp-server-mac)
- MQL5 freelance jobs request MATLAB↔MT4/5 ZeroMQ connections, which shows the pattern is common (opinion/market signal, not maintenance evidence). — [MQL5 job 122531](https://www.mql5.com/tr/job/122531)

### Inferences
- Bridge architectures fall into four types:
  - **EA + ZeroMQ.** Needs a DLL such as dingmaotu/mql-zmq, so "Allow DLL imports" must be on.
  - **EA + native MQL5 sockets.** Uses `SocketCreate`/`SocketConnect` (outbound TCP client only) and needs no DLL (background, unverified).
  - **EA + `WebRequest`.** HTTP polling to a URL on the terminal's whitelist (background, unverified).
  - **Named pipes / file exchange.**
- An EA bridge, unlike the Python package, can push events in real time from `OnTick`/`OnTradeTransaction`. That makes it the best option on MT5 for event-driven streaming.
- MetaQuotes' stated opposition to forcing DLLs into terminals (section 4) targets brokers modifying distributions, not users attaching their own DLL-using EA. Even so, DLL-free bridges carry less policy and security risk.

### Gaps
- Star counts, last-commit dates and licenses could not be checked for dingmaotu/mql-zmq, khramkov/MQL5-JSON-API, darwinex/dwxconnect or similar repos, because the GitHub API was blocked in this session.
- Native MQL5 socket limitations (client-only, no server sockets) were not confirmed from the official docs.

## 3. Cloud APIs (MetaApi)

### Takeaway
MetaApi (metaapi.cloud) hosts MT4/MT5 terminals in its cloud and exposes REST plus WebSocket streaming APIs with SDKs. It is OS-agnostic. API access to one account is free, and further usage is billed by time and reliability tier. The main risk is that you hand your MT account password to a third party. MetaApi itself suggests using the investor (read-only) password where possible.

### Cited Findings
- Offers "standard-based REST and Websocket APIs" for interacting with MetaTrader. — [MetaApi docs: client](https://metaapi.cloud/docs/client/)
- MetaApi is a paid service, but API access to one MetaTrader account is free. — [MetaApi FAQ](https://metaapi.cloud/docs/client/faq/)
- You are billed for 6 hours each time you start your server. High-reliability accounts are billed at a higher rate. The risk-management (prop) API is billed per account per hour on top. MetaApi says its pricing aims to cost no more than self-hosting. — [MetaApi risk-management FAQ](https://metaapi.cloud/docs/risk-management/faq/); [MetaApi client FAQ](https://metaapi.cloud/docs/client/faq/)
- Rate limiting is documented separately. — [MetaApi rate limiting](https://metaapi.cloud/docs/client/rateLimiting/)
- Python SDK on PyPI: `metaapi-cloud-sdk`. A Java SDK also exists. — [PyPI metaapi-cloud-sdk](https://pypi.org/project/metaapi-cloud-sdk/20.8.2); [ecosyste.ms metaapi-java-sdk](https://awesome.ecosyste.ms/projects/github.com%2Fmetaapi%2Fmetaapi-java-sdk)
- Credential exposure (vendor statement): adding an account "exposes your MT account password". MetaApi recommends the investor password where trading isn't needed. It claims an isolated, encrypted network, says production access is limited to one person, and says funds can't be withdrawn with terminal access because the broker separates deposit/withdrawal from trading access. — [MetaApi MetaStats FAQ](https://metaapi.cloud/docs/metastats/faq/)
- MetaApi also offers a Manager API, which it says is only for brokers or broker partners with MT manager access. — [metaapi.cloud](https://metaapi.cloud/) (via search extract)
- No reported MetaApi breach was found. Search hits for "MetaCloudVipNew" stealer logs are unrelated. — [Heroic breach report](https://heroic.com/darkhive-breaches/metacloudvipnew-4200-pcs-part3-stealer-log-17310-passwords-exposed/)
- Don't confuse it with MetaTraderAPI.dev, a different vendor. A third-party listing shows €499/month and a €10/month single-use tier, which may be outdated. — [GoodFirms: metatrader api](https://www.goodfirms.co/software/metatrader-api)

### Inferences
- A trading-enabled account on MetaApi means a third party holds a password that can place and close trades. A compromise could cause unauthorized trading losses even though withdrawals are blocked.
- Some broker terms may prohibit sharing credentials or third-party access. Check your broker's agreement.
- Streaming latency adds a cloud hop (broker → MetaApi terminal → your app). That is acceptable for H1/M15 gold strategies but worse than a local EA.

### Gaps
- Current per-hour prices (metaapi.cloud/#pricing) could not be retrieved.
- No independent security audit of MetaApi was found. All security claims come from the vendor.

## 4. MetaQuotes Manager / Server / Gateway / Web API, white label, and rebranding/reverse-engineering limits

### Takeaway
The Manager, Server, Gateway, Report and Web (manager REST) APIs are broker-side interfaces to an MT5 trade server. They require a server licence or manager credentials from a broker, so a retail trader cannot realistically obtain them. White labels go through licensed brokers or providers, cost thousands of USD in setup plus monthly fees, and have been restricted since late 2022. The client-terminal licence reportedly prohibits modification, derivative works, reverse engineering and decompiling, and MetaQuotes has enforced against third-party modifications and IP misuse. An individual therefore cannot legally reskin or rebrand the MT5 terminal. The legal route to a "custom MT5" is your own front-end that talks to an unmodified terminal through the official Python API or an EA bridge.

### Cited Findings
- MetaQuotes' broker page sells MT5 with White Label licensing, back-office functions, LP/exchange connectivity and "comprehensive APIs for integration with your website, trading infrastructure, and post-trade systems". — [MetaQuotes: MetaTrader 5 for Brokers](https://metaquotes.net/en/metatrader5/brokers)
- Third-party summaries say the broker APIs are the Report, Server, Gateway and Manager APIs, used for CRM, risk, reporting and account management. MT5 is deployed on the operator's own infrastructure, and MetaQuotes provides no SaaS. No public broker price table was found. — [FundedTrading: MetaTrader 5 review](https://fundedtrading.com/platform-provider/metatrader-5/)
- The MT5 Web API (Web Manager Interface, a REST API) is documented at support.metaquotes.net/en/docs/mt5/api/webapi_main, per a third-party client README. Its operations include account creation, deposits and password resets, which are manager functions. — [mt5-webapi-client README](https://cdn.jsdelivr.net/npm/mt5-webapi-client@1.0.0/README.md); [Brokeree](https://brokeree.com/?p=7642)
- `MT5Manager` (PyPI) is a Python wrapper for the Manager API, which needs manager credentials on a broker server. — [PyPI MT5Manager](https://pypi.org/project/MT5Manager/5.0.3906)
- White labels are provider-mediated. PrimeXM applies to MetaQuotes for the "standard MT5 White Label Pack" (desktop, mobile and web terminals) on the client's behalf, for a $2,000 setup fee plus $3,000/month MetaQuotes support, which MetaQuotes can raise. B2BROKER estimates $5k–$30k setup plus $1k–$10k/month. — [PrimeXM: MT5 White Label Pricing](https://primexm.com/mt5-white-label-pricing); [B2BROKER: MT5 white label costs](https://b2broker.com/news/mt5-white-label-costs/); [B2BROKER: MT5 white label cost](https://b2broker.com/news/mt5-white-label-cost/)
- MetaQuotes stopped issuing new white labels in October 2022, when MT4/MT5 were also pulled from the Apple App Store. — [FX News Group: week in review](https://fxnewsgroup.com/forex-news/retail-forex/fx-week-in-review-metatrader-removed-from-app-store-mt4-mt5-white-labels-stopped-ovalx-replaces-ceo/); [FX News Group exclusive](https://fxnewsgroup.com/?p=16576). Per B2BROKER, brokers now must go through licensed providers (vendor claim, unverified).
- Licence enforcement: MetaQuotes terminated True Forex Funds' platform licence and forced Blackbull to drop Funding Pips, citing breach of "grey label license" terms (reported, not officially confirmed by MetaQuotes). — [Finance Magnates: prop firms](https://financemagnates.com/forex/prop-trading-firms-renaissance-cutting-us-clients-integrating-new-trading-platforms)
- EULA clause (secondhand): in a notice to brokers, MetaQuotes cited its MT4/MT5 client terminal licence, which prohibits "modification, translation, creating derivative works, reverse engineering, decompiling, disassembling or hacking" of the software. MetaQuotes opposed adding DLL/EXE files to terminals, forcing DLL calls, and modifying distribution packages. — [Finance Magnates: 3rd-party developer gets red card](https://www.financemagnates.com/forex/technology/3rd-party-developer-gets-red-card-as-metaquotes-re-acts/); [Finance Magnates: MetaQuotes warns brokers about illegal plugins](https://financemagnates.com/forex/brokers/metaquotes-warns-brokers-about-illegal-plugins)
- 2013: MetaQuotes moved against the third-party plugin ecosystem and required add-ons to be vetted through its own marketplace. — [FinanceFeeds: June 3, 2013](https://financefeeds.com/day-history-june-3-2013-metaquotes-takes-swing-third-party-software-ecosystem/)
- MetaQuotes won a Cypriot court injunction against PFSoft (ProTrader) for alleged IP misuse. The order required removing files and blocking software access. The year was not stated in the extract, and no final judgment was found. — [Finance Magnates: MetaQuotes obtains injunction vs PFSoft](https://www.financemagnates.com/forex/brokers/breaking-metaquotes-obtains-injunction-pfsoft-patent-misuse/)

### Inferences
- **Individuals.** No source says an individual can buy Manager/Server/Gateway API access. Every source frames these as broker or broker-partner tools tied to a licensed server. In practice they are unavailable to a retail trader.
- **Reskinning.** Altering or rebranding the terminal binary is a derivative work or modification under the reported clause, so it is not permitted. A third-party front-end (your own UI) that calls the official Python API or an EA you wrote does not modify MetaQuotes software, which makes it the defensible route.
- **Protocol clients.** Unofficial clients of the web-terminal protocol, such as pymt5, carry legal and account risk under the anti-reverse-engineering clause and could break whenever MetaQuotes changes the protocol.
- **Naming.** Avoid "MetaTrader"/"MT5" in a product name or branding. Trademark risk is inferred; MetaQuotes has litigated domain names. — [Finance Magnates: metatrader.com domain](https://www.financemagnates.com/forex/brokers/metaquotes-loses-in-a-battle-over-metatrader-com-domain-name/)

### Gaps
- The full current MT5 EULA text could not be fetched (metatrader5.com/mql5.com were blocked). The clause wording is secondhand from Finance Magnates.
- Whether local law allows decompilation for interoperability (e.g., EU Software Directive art. 6, or India) was not researched.
- No MetaQuotes statement was found that explicitly bars individuals from white-label or API licences. That conclusion rests on how the products are structured.

## 5. Official web terminal / mobile API for embedding

### Takeaway
There is an official HTML5 MT5 Web Terminal, and MetaQuotes has promoted embedding it through an iframe widget. Since the 2022 "new Web Terminal", it runs on each broker's access server and is licensed per broker, so traders get the URL from their broker. There is no public mobile or web trading API for programmatic use. The only programmatic access via the web terminal is pymt5, which is reverse-engineered.

### Cited Findings
- An MQL5 article describes the WebTerminal as an HTML5 app embeddable "with a simple iframe widget" (sample code points to a metatraderweb.app address). It says the host site cannot access login data. The article is promotional and may be dated. — [MQL5 article 3024](https://www.mql5.com/fr/articles/3024)
- The new Web Terminal (2022) runs on the broker's access server as an individual terminal for that broker's platform only. Brokers with valid web terminal licences deploy it at no extra fee, and others order a licence via MetaQuotes support. — [MetaTrader 5 news 2253](https://metatrader5.com/en/news/2253)
- Traders are told to request the web terminal URL from their broker. It works in any browser and on iPhone/Android. — [Yahoo Finance press release](https://finance.yahoo.com/news/metatrader-5-runs-iphones-android-160100251.html)
- pymt5 drives the Web Terminal through a reverse-engineered WebSocket protocol, so it is unofficial. — [pymt5 comparison doc](https://pymt5.readthedocs.io/en/latest/python_api_detailed_comparison.html)

### Inferences
- A retail trader could embed their broker's web terminal URL in an iframe on a personal dashboard for manual trading, provided the broker's terms allow it and the page doesn't block framing. That gives a UI but no programmatic data or trade access.
- The MT5 mobile apps have no public API. Automation has to go through the desktop terminal (Python package or EA) or a cloud host (MetaApi).

### Gaps
- Current iframe parameters and whether broker-hosted terminals set X-Frame-Options/CSP could not be checked.
- No official statement on a public mobile SDK was found, so "none exists" is inferred from its absence.

## Comparison summary (for the report writer)

| Route | Market data | Account data | Trading | Real-time | OS | Needs running terminal | Licensing/risk |
|---|---|---|---|---|---|---|---|
| Official `MetaTrader5` Python | Bars, ticks, symbol info | Yes | Yes (`order_send`) | Polling only | Windows x64 (Linux/mac via Wine + mt5linux) | Yes, local | MIT package; fully sanctioned |
| EA bridge (ZeroMQ/sockets/HTTP/pipes) | Anything MQL5 can access | Yes | Yes | Event push from `OnTick` | Windows terminal (Wine/VPS possible); client any OS | Yes | Sanctioned (your own EA); DLL-based bridges need DLL imports enabled; most repos community-maintained; DWX ZMQ archived 2022 |
| MetaApi cloud | Yes | Yes | Yes | WebSocket streaming | Any | No (hosted by vendor) | Paid after 1 free account; third party holds your password |
| pymt5 (web-terminal protocol) | Yes | Yes | Yes | Push | Any | No | Reverse-engineered; EULA risk; fragile |
| Manager/Server/Gateway/Web API | Server-side | All clients | Admin | Yes | Windows server | N/A | Brokers/licensees only |
| White label / rebrand | N/A | N/A | N/A | N/A | N/A | N/A | Via broker/provider, ~$2k–30k setup + $1k–10k/mo; restricted since 2022; reskinning the binary is prohibited by EULA |
| Official Web Terminal iframe | UI only | UI only | Manual | Yes | Browser | No | Broker-licensed; no programmatic API |
