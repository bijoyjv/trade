# Code Standards (MQL5 / Pine Script)

- **MT5:** MQL5 only (not MQL4). **TradingView:** Pine Script v6 unless told otherwise.
- Expose strategy parameters as inputs (lot/risk %, SL, TP, timeframes, session filters).
- Every EA must have: stop loss on every order, max risk per trade, max spread filter, and a magic number.
- Keep signal logic identical between the Pine indicator and the MQL5 EA when they implement the same strategy.
- Explain changes step-by-step and say how to test (Strategy Tester / TradingView replay) before going live.
