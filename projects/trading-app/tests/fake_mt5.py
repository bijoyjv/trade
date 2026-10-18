"""Minimal stand-in for the MetaTrader5 package so tests run without Windows/MT5."""
from types import SimpleNamespace

import numpy as np

ACCOUNT_TRADE_MODE_DEMO, ACCOUNT_TRADE_MODE_REAL = 0, 2
TIMEFRAME_M1, TIMEFRAME_M5, TIMEFRAME_M15, TIMEFRAME_M30 = 1, 5, 15, 30
TIMEFRAME_H1, TIMEFRAME_H4, TIMEFRAME_D1 = 16385, 16388, 16408


class FakeMT5:
    def __init__(self, trade_mode=ACCOUNT_TRADE_MODE_DEMO, init_ok=True):
        for k, v in globals().items():
            if k.isupper():
                setattr(self, k, v)
        self.trade_mode, self.init_ok = trade_mode, init_ok
        self.init_kwargs, self.shut = None, False

    def initialize(self, **kw):
        self.init_kwargs = kw
        return self.init_ok

    def last_error(self):
        return (-6, "Authorization failed")

    def shutdown(self):
        self.shut = True

    def account_info(self):
        return SimpleNamespace(trade_mode=self.trade_mode, server="Exness-MT5Trial",
                               balance=10000.0, currency="USD", leverage=200)

    def symbols_get(self, pattern):
        names = {"XAUUSD*": ["XAUUSDm", "XAUUSDmicro"], "USOIL*": ["USOILm"]}.get(pattern, [])
        return tuple(SimpleNamespace(name=n) for n in names)

    def symbol_select(self, name, enable):
        return True

    def symbol_info(self, symbol):
        return SimpleNamespace(point=0.001)

    def symbol_info_tick(self, symbol):
        return SimpleNamespace(time=1760000000, bid=2650.100, ask=2650.260)

    def copy_rates_from_pos(self, symbol, tf, start, count):
        dtype = [("time", "i8"), ("open", "f8"), ("high", "f8"), ("low", "f8"), ("close", "f8"),
                 ("tick_volume", "i8"), ("spread", "i4"), ("real_volume", "i8")]
        rows = [(1760000000 + i * 900, 1.0, 2.0, 0.5, 1.5, 100, 16, 0) for i in range(count)]
        return np.array(rows, dtype=dtype)

    def positions_get(self, symbol=None):
        return ()
