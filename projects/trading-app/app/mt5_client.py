"""Thin wrapper around the MetaTrader5 package: connect, symbols, prices, candles."""
from datetime import datetime, timezone

import pandas as pd

try:
    import MetaTrader5 as mt5
except ImportError:  # non-Windows machines; tests inject a fake
    mt5 = None

from app.config import Config

TIMEFRAMES = {"M1": "TIMEFRAME_M1", "M5": "TIMEFRAME_M5", "M15": "TIMEFRAME_M15",
              "M30": "TIMEFRAME_M30", "H1": "TIMEFRAME_H1", "H4": "TIMEFRAME_H4", "D1": "TIMEFRAME_D1"}


class MT5Error(RuntimeError):
    pass


class MT5Client:
    def __init__(self, config: Config, api=None):
        self.cfg = config
        self.api = api or mt5
        if self.api is None:
            raise MT5Error("MetaTrader5 package not available (Windows only).")

    def connect(self):
        kwargs = dict(login=self.cfg.login, password=self.cfg.password, server=self.cfg.server)
        if self.cfg.mt5_path:
            kwargs["path"] = self.cfg.mt5_path
        if not self.api.initialize(**kwargs):
            raise MT5Error(f"initialize failed: {self.api.last_error()}")
        account = self.api.account_info()
        if account is None:
            raise MT5Error(f"account_info failed: {self.api.last_error()}")
        is_demo = account.trade_mode == self.api.ACCOUNT_TRADE_MODE_DEMO
        if not is_demo and not self.cfg.allow_real_account:
            self.api.shutdown()
            raise MT5Error("Real account detected. Set ALLOW_REAL_ACCOUNT=true in .env to allow it.")
        return account

    def disconnect(self):
        self.api.shutdown()

    def find_symbol(self, base: str) -> str:
        """Return the broker's symbol name for e.g. 'XAUUSD' (Exness may add a suffix like 'm')."""
        matches = self.api.symbols_get(f"{base}*") or ()
        names = sorted((s.name for s in matches), key=len)
        if not names:
            raise MT5Error(f"No symbol found for {base}")
        name = names[0]
        if not self.api.symbol_select(name, True):
            raise MT5Error(f"Could not add {name} to Market Watch")
        return name

    def tick(self, symbol: str) -> dict:
        t = self.api.symbol_info_tick(symbol)
        info = self.api.symbol_info(symbol)
        if t is None or info is None:
            raise MT5Error(f"No price for {symbol}: {self.api.last_error()}")
        return {
            "symbol": symbol,
            "time": datetime.fromtimestamp(t.time, tz=timezone.utc),
            "bid": t.bid,
            "ask": t.ask,
            "spread_points": round((t.ask - t.bid) / info.point),
        }

    def candles(self, symbol: str, timeframe: str = "M15", count: int = 200) -> pd.DataFrame:
        tf = getattr(self.api, TIMEFRAMES[timeframe])
        rates = self.api.copy_rates_from_pos(symbol, tf, 0, count)
        if rates is None or len(rates) == 0:
            raise MT5Error(f"No candles for {symbol} {timeframe}: {self.api.last_error()}")
        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
        return df[["time", "open", "high", "low", "close", "tick_volume", "spread"]]

    def positions(self, symbol: str | None = None):
        result = self.api.positions_get(symbol=symbol) if symbol else self.api.positions_get()
        return list(result or ())
