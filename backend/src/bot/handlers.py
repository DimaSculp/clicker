from aiogram import Router
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from confige_reader import confige

from confige_reader import confige

router = Router()

markup = (
    InlineKeyboardBuilder()
    .button(text=" ⚙️ open", web_app=WebAppInfo(url=f"{confige.WEBAPP_URL}"))
).as_markup()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("lets click!", reply_markup=markup)
