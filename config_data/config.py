import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class TgBot:
    token: str
    admin_id: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(
        token=os.getenv('TOKEN'),
        admin_id=list(map(int, os.getenv('ADMIN_ID')))
    ))
