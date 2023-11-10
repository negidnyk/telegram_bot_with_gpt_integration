
def save_output(file_path):
    out_path = r"C:\Users\Артем\PycharmProjects\testopenai\output.py"
    try:
        # Read the Python code from the text file
        with open(file_path, "r") as text_file:
            python_code = text_file.read()

        with open(out_path, "a") as python_file:
            python_file.write(python_code)

        print("Conversion successful.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_variable_as_txt_file(text):
    # Step 1: Convert the variable to a string representation
    data_str = str(text)  # Convert to a string

    # Step 2: Open a text file for writing using 'with'
    file_path = r"C:\Users\Артем\PycharmProjects\testopenai\output.txt"  # Specify the file path
    with open(file_path, "w") as file:
        # Step 3: Write the variable to the text file
        file.write(data_str)

    print(f"Variable saved to '{file_path}' as a text file.")

    # Uncomment the following line to call save_output(file_path)
    # save_output(file_path)

    return file_path


def get_file_text():
    with open(r"C:\Users\Артем\PycharmProjects\testopenai\output.txt", "r") as text_file:
        python_code = text_file.read()
    return python_code


def filter_response(original_code):

    modified_string = ""

    top_characters_to_find = ["```python", "```Python"]
    bottom_character_to_find = "```"

    for character in top_characters_to_find:
        top_position = original_code.find(character)
        if top_position != -1:
            modified_string = original_code[top_position + 9:]


    bottom_position = modified_string.find(bottom_character_to_find)
    if bottom_position != -1:
        modified_string = modified_string[:bottom_position]
        # Save the modified_string as a txt file here (you need to implement this function)
        return modified_string
    else:
        print("Нижний символ не найден в строке.")
        return modified_string
