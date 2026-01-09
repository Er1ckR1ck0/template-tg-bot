from aiogram import F, Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=f"Приветики-пистолетики! {message.from_user.full_name}")


@router.message(F.text)
async def echo(message: Message):
    await message.answer(text=f"{message.text}")
