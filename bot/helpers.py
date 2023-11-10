import codecs


async def get_code_from_current_file():

    file_path = r"C:\Users\Артем\PycharmProjects\testopenai\bot\bot_messages_handler.py"
    file = codecs.open(file_path, "r", "utf-8")
    data = file.read()
    file.close()
    return data


async def get_code_from_file(path):
    try:
        with open(path, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
