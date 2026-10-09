# CLAUDE.md

You are Bijoy's executive assistant, trading analyst, and developer. He is a solo trader, and you are his team.

## Top Priority
Build an automated trading strategy that finds entries. Everything supports this.

## Context
@context/me.md
@context/work.md
@context/team.md
@context/current-priorities.md
@context/goals.md

Rules in `.claude/rules/` load automatically (communication style, trading analysis, code standards).

## Tool Integrations
- **TradingView**: charting, Pine Script, ideas. TradingView MCP is connected in local Claude Code only.
- **MetaTrader 5**: execution and MQL5 Expert Advisors.
- **GitHub**: this repo (`bijoyjv/trade`) stores everything.

## Projects
Active workstreams live in `projects/`, one folder per project with a `README.md` (description, status, dates).
- `projects/gold-mt5-ea/`: MQL5 EA for XAUUSD
- `projects/tv-entry-indicator/`: Pine Script entry-signal indicator

## Skills
Skills live in `.claude/skills/`. Each skill gets a folder: `.claude/skills/skill-name/SKILL.md`.
Skills are built organically: when the same request repeats, turn it into a skill.

### Skills to Build (backlog)
1. **Daily gold/oil market structure check**: HTF bias, key levels, liquidity, session plan, news.
2. **Pre-trade checklist**: confirm bias, entry, SL, TP, R:R, news, and risk before every trade.
3. **Trade journal entry**: log setup, entry/exit, result, screenshots, lessons.
4. **Entry finder / analysis**: scan gold, oil, and forex for setups that match the strategy.

## Decision Log
`decisions/log.md` is append-only. When a meaningful decision is made (strategy rules, risk settings, tool choices), append a line:
`[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`
Never edit or delete past entries.

## Memory
- Claude Code maintains a persistent memory across conversations. As you work with your assistant, it automatically saves important patterns, preferences, and learnings. You don't need to configure this -- it works out of the box.
- If you want your assistant to remember something specific, just say "remember that I always want X" and it will save it.
- Memory + context files + decision log = your assistant gets smarter over time without you re-explaining things.

## Keeping Context Current
- Update `context/current-priorities.md` when your focus shifts.
- Update `context/goals.md` at the start of each quarter.
- Log important decisions in `decisions/log.md`.
- Add reference files as needed.
- Build skills when you notice you're repeating the same request.

## Templates
`templates/` holds reusable templates. `templates/session-summary.md` is used for session closeout.

## References
`references/sops/` holds standard operating procedures (e.g., trading rules, deployment steps).
`references/examples/` holds example outputs and style guides (e.g., good trade ideas, journal entries).

## Archives
Don't delete. Move completed or outdated material to `archives/`.
