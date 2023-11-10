import os
from aiogram import Router, types
import openai
from chatgpt_logic.chatgpt_developer import generate_response
from chatgpt_logic.chatgpt_tester import testing_code
from chatgpt_logic.helpers import save_output, save_variable_as_txt_file, filter_response, get_file_text
from chatgpt_logic.chatgpt_ideas import generate_ideas
from bot.helpers import get_code_from_current_file, get_code_from_file


# Get result code button. Returns a string with code from output.py file
async def get_result(message):
    result = await get_code_from_file(r'C:\Users\Артем\PycharmProjects\testopenai\output.py')
    return result


# Rebuild bot with new code button function. It gets current code from bot_messages_handler.py file and new features
# from output.py file. Then it links both pieces of code and sends to opeanai API ti fix bugs.
# When the code is fixed, function writes the new fixed code to the output.py file and calls main.py to restart bot
async def rebuild_a_bot(message: types.Message, conv_history):

    additional_code_file_path = r"C:\Users\Артем\PycharmProjects\testopenai\output.py"

    additional_code = await get_code_from_file(additional_code_file_path)
    print(f"#######################Additional code:\n{additional_code}\n##########################\n")

    current_code = await get_code_from_current_file()
    print(f"#######################Current code:\n{current_code}\n##########################\n")


    with open(additional_code_file_path, "w") as file:
        # Step 3: Write the variable to the text file
        file.write(current_code)

    with open(additional_code_file_path, "a") as file:
        # Step 3: Write the variable to the text file
        if additional_code is None:
            additional_code = ""
        else:
            file.write(additional_code)

    result_code = await get_code_from_file(additional_code_file_path)

    print(f"#######################Result code:\n{result_code}\n##########################\n")

    await message.answer("System: Need to test the code before rebuilding\nGiving it to the tester...")

    await message.answer(f'Tester: Got it! Start testing..')
    await message.answer("Tester starts testing...\nWait a little =)")

    tester_request = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f'''Find and fix bugs in this Python code:{result_code} . 
    Return fixed Python code as a single file. Do not split it.'''}],
        max_tokens=1500
    )

    tester_resposne = tester_request.choices[0].message["content"]


    # tested_result_code = testing_code(result_code, conversation)
    await message.answer(f'Tester: I`ve finished testing this code!')

    filtered_result_code = filter_response(tester_resposne)

    if filtered_result_code:
        await message.answer(f'System: Saving tested code...')

        with open(additional_code_file_path, "w") as file:
            # Step 3: Write the variable to the text file
            file.write(filtered_result_code)
        await message.answer(f'System: Code is saved to the file...')
        await message.answer("System: Restarting the bot with new features")
        os.startfile(r'C:\Users\Артем\PycharmProjects\testopenai\main.py')
        # await run_script_in_current_directory()
        await message.answer("System: Bot is successfully restarted with new features")

        conv_history.clear()
    else:
        await message.answer(
            f'System: It looks something went wrong(("')
        conv_history.clear()


# Generate code iteration button function
async def generate_code(message, conversation):
    code = await get_code_from_current_file()
    print(code)

    # Start initialization of conversation theme block
    conversation.append({"role": "system", "content": f"Our task is adding new features to Python code which will be"
                                                              f" provided by user. We have to add new features to the bootom"
                                                              f" of submitted code"})
    conversation.append({"role": "user", "content": f"There is Python code to be improved {code}"})
    conversation.append({"role": "assistant", "content": "Sure, one moment!"})
    # End initialization of conversation theme block

    # Start idea generator block
    await message.answer("Idea generator: Got it! Start thinking...")
    await message.answer("Idea generator starts thinking...\nWait a little =)")
    ideas = generate_ideas(conversation, code)
    await message.answer(f"Idea generator: There are some ideas we can implement:\n{ideas}\nGiving the ideas to "
                                 f"developer...")
    # End idea generator block

    # Start developer block
    await message.answer("Developer: OK! Got it =)\nWait a little...")
    await message.answer("Developer starts working...")
    new_code = generate_response(conversation, ideas, code)
    await message.answer(f'Developer: I`ve created some code:\nGiving it to the tester...')
    # End developer block

    # Start tester block
    await message.answer(f'Tester: Got it! Start testing..')
    await message.answer("Tester starts testing...\nWait a little =)")
    tested_code = testing_code(new_code, conversation)
    await message.answer(f'Tester: I`ve tested this code.\nNow we should save it to the file with improvements...')
    # End tester block

    # Start saving progress to the file block
    await message.answer(f'System: I will write new code to the file to save progress...')
    filtered_code = filter_response(tested_code)
    print(f"Итоговый фильтрованный код: {filtered_code}")

    if filtered_code is not None or filtered_code != "":
        await message.answer(f'System: Start saving...')
        txt_path = save_variable_as_txt_file(filtered_code)
        save_output(txt_path)
        await message.answer(f'System: Code is saved to the file...\nNow you can run "Generate code iteartion" again to genereate more new features!')
        conversation.clear()
    else:
        await message.answer(f'System: It looks like the code has bad quality(\nPlease, run "Generate code iteartion" command to try again!"')
        conversation.clear()

