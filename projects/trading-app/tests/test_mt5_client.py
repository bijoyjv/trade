import pytest

from app.config import Config
from app.mt5_client import MT5Client, MT5Error
from tests.fake_mt5 import ACCOUNT_TRADE_MODE_REAL, FakeMT5


def make(api, allow_real=False):
    cfg = Config(login=1, password="p", server="Exness-MT5Trial", mt5_path=None,
                 allow_real_account=allow_real)
    return MT5Client(cfg, api=api)


def test_connect_demo_ok():
    api = FakeMT5()
    acc = make(api).connect()
    assert acc.server == "Exness-MT5Trial"
    assert "path" not in api.init_kwargs


def test_connect_failure_raises():
    with pytest.raises(MT5Error, match="Authorization failed"):
        make(FakeMT5(init_ok=False)).connect()


def test_real_account_blocked_by_default():
    api = FakeMT5(trade_mode=ACCOUNT_TRADE_MODE_REAL)
    with pytest.raises(MT5Error, match="Real account"):
        make(api).connect()
    assert api.shut


def test_real_account_allowed_when_enabled():
    make(FakeMT5(trade_mode=ACCOUNT_TRADE_MODE_REAL), allow_real=True).connect()


def test_find_symbol_picks_shortest_suffix():
    assert make(FakeMT5()).find_symbol("XAUUSD") == "XAUUSDm"


def test_find_symbol_missing():
    with pytest.raises(MT5Error):
        make(FakeMT5()).find_symbol("BTCXYZ")


def test_tick_spread_in_points():
    t = make(FakeMT5()).tick("XAUUSDm")
    assert t["spread_points"] == 160


def test_candles_dataframe():
    df = make(FakeMT5()).candles("XAUUSDm", "M15", 5)
    assert len(df) == 5
    assert list(df.columns) == ["time", "open", "high", "low", "close", "tick_volume", "spread"]
    assert str(df["time"].dt.tz) == "UTC"
