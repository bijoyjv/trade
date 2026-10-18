# Decision Log


Append-only. When a meaningful decision is made, log it here.


Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...


---
[2026-10-18] DECISION: Connect custom app to Exness through the official MetaTrader5 Python package and a running MT5 terminal | REASONING: Official, free, data stays on PC; reverse engineering MT5 is prohibited by its licence | CONTEXT: projects/trading-app
[2026-10-18] DECISION: Rule-based engine places trades; AI (Claude) only analyses and filters, outside the instant entry path | REASONING: LLM calls are slow (seconds) and non-deterministic; entries must be fast and testable | CONTEXT: projects/trading-app
[2026-10-18] DECISION: Demo account only by default; real account requires ALLOW_REAL_ACCOUNT=true | REASONING: Prevent accidental live trading before backtesting and demo results | CONTEXT: projects/trading-app
