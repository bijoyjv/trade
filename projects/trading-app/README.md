# Trading App

Custom trading app with TradingView-style charts, Python indicators, and a rule-based algo bot
connected to an Exness MT5 account. AI (Claude) analyses and filters; the rule engine trades.

- **Status:** Active (Step 1)
- **Started:** 2026-10-18
- **Platform:** Windows PC, MT5 terminal logged into Exness, Python 3.10+

## Build Steps
| # | Step | Status |
|---|------|--------|
| 1 | Connect to Exness via MT5, read account, symbol, price, candles | Built, test on PC |
| 2 | Risk gate + order placement (demo only), timing log | Next |
| 3 | Local data storage (SQLite) | |
| 4 | Chart UI (FastAPI + Lightweight Charts) | |
| 5 | Python indicator engine (Pine-like) | |
| 6 | Backtester | |
| 7 | Bot: alerts mode, then confirm mode on demo | |
| 8 | AI layer (Claude via MCP) + n8n | |

## Step 1: Run on your PC
1. Install Python 3.10+ (64-bit) and MT5. Log into your **Exness demo** account in MT5 once.
2. Open a terminal in this folder and run:
   ```
   pip install -r requirements.txt
   copy .env.example .env
   ```
3. Edit `.env`: fill in login, password, and server (copy server name exactly from Exness Personal Area).
4. Run:
   ```
   python scripts/check_connection.py
   ```
5. Expected output: account info, the gold symbol name (e.g. `XAUUSDm`), live bid/ask/spread, last 5 M15 candles.
6. Send me the output (remove the account number if you like).
