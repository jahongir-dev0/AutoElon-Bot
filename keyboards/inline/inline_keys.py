from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_bnt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python", callback_data="py"),
            InlineKeyboardButton(text="C#", callback_data="sharp"),
            InlineKeyboardButton(text="C++", callback_data="cplus"),
            InlineKeyboardButton(text="Java", callback_data="java"),
            InlineKeyboardButton(text="Go", callback_data="go")
        ]
    ]
)
