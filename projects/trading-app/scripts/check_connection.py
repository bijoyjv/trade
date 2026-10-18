"""Step 1 check: connect to Exness via MT5 and print account, gold price, and candles."""
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import load_config
from app.mt5_client import MT5Client, MT5Error

IST = ZoneInfo("Asia/Kolkata")


def main():
    client = MT5Client(load_config())
    try:
        acc = client.connect()
        print(f"Connected: {acc.server} | {'DEMO' if acc.trade_mode == client.api.ACCOUNT_TRADE_MODE_DEMO else 'REAL'} | "
              f"balance {acc.balance} {acc.currency} | leverage 1:{acc.leverage}")
        for base in ("XAUUSD", "USOIL"):
            try:
                sym = client.find_symbol(base)
            except MT5Error as e:
                print(f"{base}: {e}")
                continue
            t = client.tick(sym)
            print(f"{sym}: bid {t['bid']} ask {t['ask']} spread {t['spread_points']} pts "
                  f"at {t['time'].astimezone(IST):%Y-%m-%d %H:%M:%S} IST")
            df = client.candles(sym, "M15", 5)
            df["time"] = df["time"].dt.tz_convert(IST)
            print(df.to_string(index=False))
        print(f"Open positions: {len(client.positions())}")
    except MT5Error as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
