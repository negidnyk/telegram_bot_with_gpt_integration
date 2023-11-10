from aiogram import Bot, Dispatcher, Router, types
import openai
from config import OPENAI_KEY

# Встановлення API ключа OpenAI
openai.api_key = OPENAI_KEY


def testing_code(developer_response, conversation):
    print("Tester starts testing...")

    tester_request = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f'''Find and fix bugs in this Python code:{developer_response} . 
    Return fixed Python code as a single file. Do not split it.'''}],
        max_tokens=1500
    )

    tester_resposne = tester_request.choices[0].message["content"]

    print(f'Tester response: {tester_resposne}')

    conversation.append({"role": "assistant", "content": tester_resposne})

    print("Tester has already ended his work. Now you can check out the code in file")

    return tester_resposne
