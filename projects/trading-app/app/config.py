import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    login: int
    password: str
    server: str
    mt5_path: str | None
    allow_real_account: bool


def load_config() -> Config:
    load_dotenv()
    missing = [k for k in ("EXNESS_LOGIN", "EXNESS_PASSWORD", "EXNESS_SERVER") if not os.getenv(k)]
    if missing:
        raise SystemExit(f"Missing in .env: {', '.join(missing)}")
    return Config(
        login=int(os.environ["EXNESS_LOGIN"]),
        password=os.environ["EXNESS_PASSWORD"],
        server=os.environ["EXNESS_SERVER"],
        mt5_path=os.getenv("MT5_PATH") or None,
        allow_real_account=os.getenv("ALLOW_REAL_ACCOUNT", "false").lower() == "true",
    )
