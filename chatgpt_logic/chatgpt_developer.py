import openai
from config import OPENAI_KEY

# Встановлення API ключа OpenAI
openai.api_key = OPENAI_KEY


def generate_response(conv_history, ideas, previous_code):
    print('Developer is creating a code...')

    # Generate a response
    developer_request = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                     messages=[{"role": "user", "content": f'''Add this new 
                                                     functionality: {ideas} to this Python code: {previous_code} . 
                                                     Return only code of new features as a single Python file in answer. 
                                                     Do not split it'''}],
                                                     max_tokens=1500
                                                     )

    developer_reply = developer_request.choices[0].message["content"]

    conv_history.append({"role": "assistant", "content": developer_reply})

    print(f"Developer response: {developer_reply}")

    return developer_reply


