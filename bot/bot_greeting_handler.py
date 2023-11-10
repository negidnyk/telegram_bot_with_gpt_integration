from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from bot.navigation_menu.buttons import mainMenu


greetings_router = Router()


@greetings_router.message(CommandStart())
async def get_start(message: types.Message, bot: Bot):
    await message.answer(f'''Hi, {message.from_user.first_name}!\nI will be happy to create some code for you!\n
Choose "Generate code iteration" option to start generating code\nTo stop the bot, choose option "Stop".\nWaiting for your choise:''', reply_markup=mainMenu)



