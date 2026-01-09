from typing import List, Optional, Union

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Telegram(BaseSettings):
    model_config = SettingsConfigDict(
        str_to_upper=True,
        env_file=".env",
        env_prefix="Telegram",
        env_file_encoding="UTF-8",
    )

    BOT_TOKEN: SecretStr
    ADMIN_IDS: str | List[str]  # That's token we'll add to db
