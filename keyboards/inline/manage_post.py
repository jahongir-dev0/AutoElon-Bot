from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# CallbackData obyekti (action va post id parametrlari)
post_callback = CallbackData("post", "action")

# Foydalanuvchi uchun tasdiqlash tugmalari
confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📤 Chop etish", callback_data=post_callback.new(action="post")),
            InlineKeyboardButton("❌ Bekor qilish", callback_data=post_callback.new(action="cancel"))
        ]
    ]
)

# Admin uchun tugmalar (Agar admin bo'lsa, qo'llaniladi)
admin_confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Chop etish", callback_data=post_callback.new(action="admin_post")),
            InlineKeyboardButton("❌ Bekor qilish", callback_data=post_callback.new(action="admin_cancel"))
        ]
    ]
)