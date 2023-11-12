from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def get_main_kb():
    main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add("Ask the AI 🧠").add("Get developers socials 📱")\
            .add("Report the problem ⛔")
    return main_keyboard


def get_return_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Return to menu")
    return kb


def get_developer_socials():
    inline = InlineKeyboardMarkup(row_width=1)
    inline.add(
        InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/_rasikrr_/")
    )
    return inline
