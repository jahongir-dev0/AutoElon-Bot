from aiogram import types

from keyboards.inline.inline_keys import inline_bnt
from loader import dp
from states.sign_up import sign


@dp.message_handler(text="Royxatdan O'tish 🪧")
async def reply_royhat(message: types.Message):
    await message.answer("Iltimos, ismingizni kiriting: ")
    await sign.name.set()


@dp.message_handler(text="Bot Haqida ℹ️")
async def reply_royhat(message: types.Message):
    await message.answer(
        "<b>BU bot Avtomabillarni Reklama qilish uchun!!!</b> <i>AvtoAdmin</i> <a href=\"https://t.me/just_aware\" >Telegram</a> ")

@dp.message_handler(text="Kurslar")
async def reply_royhat(message: types.Message):
    await message.answer(
        "<b>Quyida bizning kurslar bilan tanishasiz!!!</b>",reply_markup=inline_bnt)


@dp.callback_query_handler(text="py")
async def callback_button(call: types.CallbackQuery):
    await call.message.answer("Siz python kursini tanladingiz!")
