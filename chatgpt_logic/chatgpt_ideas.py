from aiogram import Bot, Dispatcher, Router, types
import openai
from config import OPENAI_KEY

# Встановлення API ключа OpenAI
openai.api_key = OPENAI_KEY


def generate_ideas(conversation, developer_response):
    print("Idea generator is thinking...")

    # if developer_response is not None:
    conversation.append({"role": "user", "content": f'''Brainstorm some ideas to extend functionality of this 
    Python code:{developer_response}. Return a list with 3 ideas to be implemented'''})

    idea_generator_request = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=600
    )

    idea_generator_resposne = idea_generator_request.choices[0].message["content"]

    print(f'Idea generator response: {idea_generator_resposne}')

    conversation.append({"role": "assistant", "content": idea_generator_resposne})

    print("Idea generator has already ended his work.")

    return idea_generator_resposne

