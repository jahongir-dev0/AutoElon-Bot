from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Royxatdan O'tish 🪧",),
            KeyboardButton(text="Avto Post 🚘"),

        ],
        [
            KeyboardButton(text="Bot Haqida ℹ️"),
        ]

    ], resize_keyboard=True
)