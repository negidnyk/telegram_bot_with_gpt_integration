from config import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bot.bot_greeting_handler import greetings_router
from bot.bot_messages_handler import messages_router

# Setting bot token form .env file
TOKEN = BOT_TOKEN


async def start():
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(greetings_router)
    dp.include_router(messages_router)
    # And the run events dispatching
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



