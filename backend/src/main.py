
from os import getenv
from typing import AsyncGenerator
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Update
from fastapi import FastAPI, Request
from tortoise import Tortoise

from confige_reader import confige

from bot import settup_routes
import uvicorn
TOKEN = getenv("6990416804:AAEMpdItV2zQD8Td83FAJ2IBTgRjfeh8xSQ")
bot = Bot("6990416804:AAEMpdItV2zQD8Td83FAJ2IBTgRjfeh8xSQ")
from tortoise import Tortoise

async def init():
    await Tortoise.init(
        db_url="mysql://sql8715319:rHYYAEhVut@sql8.freemysqlhosting.net:3306/sql8715319",
        modules={"models": ["db.models.user"]}
    )
    await Tortoise.generate_schemas()

async def lifespan(app: FastAPI) -> AsyncGenerator:
    await bot.set_webhook(
        url="https://2f72-5-166-39-43.ngrok-free.app",
        drop_pending_updates=True
    )
    await init()  # Вызов функции init
    yield
    await Tortoise.close_connections()
    await bot.session.close()

# Остальной код...

dp = Dispatcher()
app = FastAPI(lifespan=lifespan)
  # Assuming 'resolve_used_types' is the correct attribute or method name

dp.include_router(settup_routes())

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot,update)

if __name__ == "__main__":
    uvicorn.run(app)