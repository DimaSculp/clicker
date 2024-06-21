import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Confige(BaseSettings):
    BOT_TOKEN: str = "6990416804:AAEMpdItV2zQD8Td83FAJ2IBTgRjfeh8xSQ"
    DB_URL: str=""
    WEBHOOK_URL: str="https://2f72-5-166-39-43.ngrok-free.app"
    WEBAPP_URL: str="https://e06c-5-166-39-43.ngrok-free.app"
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",                              
        env_file=os.path.join(os.path.dirname(__file__), ".env"))
        

confige = Confige()