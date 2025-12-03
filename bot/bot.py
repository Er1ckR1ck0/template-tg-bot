import os
import logging
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from client.handlers.start import router as start_router


load_dotenv()


async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    
    dp.include_router(start_router)
    
    await bot.delete_webhook()
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    asyncio.run(main())
    