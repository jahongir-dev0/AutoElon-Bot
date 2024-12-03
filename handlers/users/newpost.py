import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from states.newpost import NewPost
from keyboards.inline.manage_post import confirmation_keyboard, post_callback, admin_confirmation_keyboard
from keyboards.default.def_tugma import menu
from loader import dp, bot

logging.basicConfig(level=logging.INFO)

# Post ko'rinishi generatsiya qilish uchun funksiya
def generate_post_preview(data):
    return (
        f"<b>🚗 Avto:</b> {data['avto']}\n"
        f"<b>📅 Yili:</b> {data['yil']}\n"
        f"<b>👣 Probeg:</b> {data['probeg']} km\n"
        f"<b>💎 Kraska:</b> {data['kraska']}\n"
        f"<b>⛽️ Benzin:</b> {data['benzin']}\n"
        f"<b>💰 Narxi:</b> {data['narx']} $\n"
        f"<b>☎️ Tel:</b> {data['tel']}\n"
        f"<b>🏠 Manzil:</b> {data['manzil']}\n"
    )

# Post yaratishni boshlash
@dp.message_handler(text="Avto Post 🚘")
async def create_post(message: Message):
    await message.answer("🚗 Avtomobil nomini kiriting:")
    await NewPost.Avto.set()

# Ketma-ket barcha holatlarni ko'rib chiqish
@dp.message_handler(state=NewPost.Avto)
async def enter_avto(message: Message, state: FSMContext):
    await state.update_data(avto=message.text)
    await message.answer("📅 Yilini kiriting:")
    await NewPost.Yil.set()

@dp.message_handler(state=NewPost.Yil)
async def enter_year(message: Message, state: FSMContext):
    await state.update_data(yil=message.text)
    await message.answer("👣 Probegini kiriting (km):")
    await NewPost.Probeg.set()

@dp.message_handler(state=NewPost.Probeg)
async def enter_probeg(message: Message, state: FSMContext):
    await state.update_data(probeg=message.text)
    await message.answer("💎 Kraskasini kiriting:")
    await NewPost.Kraska.set()

@dp.message_handler(state=NewPost.Kraska)
async def enter_kraska(message: Message, state: FSMContext):
    await state.update_data(kraska=message.text)
    await message.answer("⛽️ Benzin turini kiriting:")
    await NewPost.Benzin.set()

@dp.message_handler(state=NewPost.Benzin)
async def enter_benzin(message: Message, state: FSMContext):
    await state.update_data(benzin=message.text)
    await message.answer("💰 Narxini kiriting ($):")
    await NewPost.Narx.set()

@dp.message_handler(state=NewPost.Narx)
async def enter_price(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("☎️ Telefon raqamini kiriting:")
    await NewPost.Tel.set()

@dp.message_handler(state=NewPost.Tel)
async def enter_phone(message: Message, state: FSMContext):
    await state.update_data(tel=message.text)
    await message.answer("🏠 Manzilini kiriting:")
    await NewPost.Manzil.set()

@dp.message_handler(state=NewPost.Manzil)
async def enter_address(message: Message, state: FSMContext):
    await state.update_data(manzil=message.text)
    await message.answer("📸 Avtomobilingiz rasmini yuboring:")
    await NewPost.AvtoRasm.set()

# Rasm qabul qilish
@dp.message_handler(state=NewPost.AvtoRasm, content_types=types.ContentType.PHOTO)
async def enter_avto_photo(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo_id=photo_id)

    data = await state.get_data()
    post_preview = generate_post_preview(data)

    # Postni tayyorlash
    if 'photo_id' in data:
        await message.answer_photo(data['photo_id'], caption=f"Tayyor post:\n\n{post_preview}", reply_markup=confirmation_keyboard)
    else:
        await message.answer(f"Tayyor post:\n\n{post_preview}", reply_markup=confirmation_keyboard)

    await NewPost.Confirm.set()

# Foydalanuvchi tasdiqlagan postni adminlarga yuborish
@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def send_post_to_admin(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    post_preview = generate_post_preview(data)

    for admin in ADMINS:
        if 'photo_id' in data:
            await bot.send_photo(admin, data['photo_id'], caption=post_preview, reply_markup=admin_confirmation_keyboard)
        else:
            await bot.send_message(admin, post_preview, reply_markup=admin_confirmation_keyboard)

    await callback_query.answer("Post adminlarga yuborildi. Iltimos, tasdiqlashni kuting.", show_alert=True)
    await state.finish()

# Admin postni kanalga yuborishi
@dp.callback_query_handler(post_callback.filter(action="admin_post"))
async def confirm_post_admin(callback_query: CallbackQuery):
    message = callback_query.message

    if message.photo:
        await bot.send_photo(CHANNELS[0], message.photo[-1].file_id, caption=message.caption)
    else:
        await bot.send_message(CHANNELS[0], message.text)

    await callback_query.answer("Post kanalga muvaffaqiyatli yuborildi!", show_alert=True)
    await callback_query.message.answer("Bosh Menu", reply_markup=menu)

# Admin postni bekor qilishi
@dp.callback_query_handler(post_callback.filter(action="admin_cancel"))
async def cancel_post_admin(callback_query: CallbackQuery):
    await callback_query.answer("Post bekor qilindi.", show_alert=True)
    await callback_query.message.answer("Bosh Menu", reply_markup=menu)