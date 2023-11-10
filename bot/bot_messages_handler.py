from aiogram import Router, types
import openai
from config import OPENAI_KEY
from aiogram import F
from bot.services import rebuild_a_bot, generate_code, get_result


messages_router = Router()

# Встановлення API ключа OpenAI
openai.api_key = OPENAI_KEY

conversation = []


@messages_router.message(F.text.lower() == "stop")
async def stop_bot(message: types.Message):
    await message.answer("OK! Looking froward to the next task!")


@messages_router.message(F.text.lower() == "help")
async def stop_bot(message: types.Message):
    await message.answer(f'''This bot can generate a code to improve itself.\nUse "Generate code iteration" option to 
generate some code to improve me.\nChoose "Stop" option to finish work.\nChoose "Rebuild bot with new code" option to 
add code of improvements to me and restart.\nChoose "Send result code" option to get current bot code.''')


@messages_router.message(F.text.lower() == "rebuild bot with new code")
async def rebuild_bot(message: types.Message):
    await rebuild_a_bot(message, conversation)


@messages_router.message(F.text.lower() == "generate code iteration")
async def code_generation(message: types.Message):
    await generate_code(message, conversation)


@messages_router.message(F.text.lower() == "send result code")
async def send_result_code(message: types.Message):
    result = await get_result(message)
    try:
        await message.answer(result)
    except Exception as e:
        await message.answer(str(e))








