from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# --- Main menu ---

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder="Manage the bot using buttons",
                               selective=True,
                               keyboard=[[KeyboardButton(text="/start"),
                                          KeyboardButton(text="Generate code iteration"),
                                          KeyboardButton(text="Rebuild bot with new code"),
                                          KeyboardButton(text="Stop"),
                                          KeyboardButton(text="Send result code"),
                                          KeyboardButton(text="Help")]])
