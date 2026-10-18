# MetaTrader5 Python Package: Reference

**Source:** official package `MetaTrader5` v5.0.6231 from PyPI (inspected 2026-10-18).
Full docs: https://www.mql5.com/en/docs/python_metatrader5 (blocked from cloud sessions; read locally).

## Requirements
- Windows x64 only. The MT5 terminal must be installed, running, and logged in.
- Talks to the local terminal over IPC. No push/callback API: real-time data means polling.

## Functions
| Group | Functions |
|-------|-----------|
| Connection | `initialize(path, login, password, server, timeout, portable)`, `login`, `shutdown`, `version`, `last_error` |
| Account / terminal | `account_info`, `terminal_info` |
| Symbols | `symbols_total`, `symbols_get`, `symbol_info`, `symbol_info_tick`, `symbol_select` |
| Market depth | `market_book_add`, `market_book_get`, `market_book_release` |
| Bars | `copy_rates_from`, `copy_rates_from_pos`, `copy_rates_range` |
| Ticks | `copy_ticks_from`, `copy_ticks_range` (`COPY_TICKS_ALL / INFO / TRADE`) |
| Open orders | `orders_total`, `orders_get` |
| Positions | `positions_total`, `positions_get` |
| History | `history_orders_total`, `history_orders_get`, `history_deals_total`, `history_deals_get` |
| Trading | `order_calc_margin`, `order_calc_profit`, `order_check`, `order_send` |

## Constants
- Timeframes: `TIMEFRAME_M1` ... `TIMEFRAME_MN1` (M1-M6, M10, M12, M15, M20, M30, H1-H4, H6, H8, H12, D1, W1, MN1).
- Order types: market, limit, stop, stop-limit, close-by.
- Trade actions: `DEAL`, `PENDING`, `SLTP`, `MODIFY`, `REMOVE`, `CLOSE_BY`.
- Filling: `FOK`, `IOC`, `RETURN`, `BOC`. Expiry: `GTC`, `DAY`, `SPECIFIED`, `SPECIFIED_DAY`.

## Warning: built-in `Buy` / `Sell` / `Close` helpers
The package ships helpers `Buy()`, `Sell()`, `Close()`. Do **not** use them in our app:
1. They send market orders with **no stop loss** (breaks our EA rule: SL on every order).
2. They retry up to 10 times on requote, automatically.
3. Deviation is hard-coded to 10 points.

Use `order_check()` then `order_send()` with an explicit `sl`, `tp`, `magic`, `deviation`, and `type_filling`, through our risk gate.
