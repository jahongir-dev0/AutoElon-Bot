from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="Royxatdan o'tish📤"),
            KeyboardButton(text="Bot haqida❕"),
            KeyboardButton(text="Kurslar"),

        ],
        [
            KeyboardButton(text="Statistika⚡"),
            KeyboardButton(text="Hamyon💸"),

        ]


    ],
    resize_keyboard=True
)
