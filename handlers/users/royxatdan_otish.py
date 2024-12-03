from aiogram import types
import re
from loader import dp
from aiogram.dispatcher import FSMContext
from states.sign_up import sign


@dp.message_handler(commands=['sign_up'])
async def sign_up_command(message: types.Message):
    await message.answer("Iltimos, ismingizni kiriting: ")
    await sign.name.set()  # hozir ism kiritish holatiga otdi


@dp.message_handler(state=sign.name)
async def set_name(message: types.Message, state: FSMContext):
    user_name = message.text
    pattern=r'[A-Z]{1}[a-z]'
    if re.match(pattern,user_name):
        async with state.proxy() as data:
            data['name'] = user_name
        await sign.next()
        await message.answer("Yoshingizni kiriting")

    else:
        await message.answer("Iltimos, ismingizni to'g'ri kiriting: ")




@dp.message_handler(state=sign.age)
async def set_name(message: types.Message, state: FSMContext):
    age = message.text
    async with state.proxy() as data:
        data['age'] = age
    await sign.next()
    await message.answer("Telefon raqamingizni kiriting")


@dp.message_handler(state=sign.phone)
async def set_name(message: types.Message, state: FSMContext):
    phone = message.text
    async with state.proxy() as data:
        data['phone'] = phone
    await sign.next()
    await message.answer("Emailingizni kiriting")


@dp.message_handler(state=sign.email)
async def set_name(message: types.Message, state: FSMContext):
    email = message.text
    async with state.proxy() as data:
        data['email'] = email
        await message.answer(
            f"Ismingiz: {data['name']}\nYoshingiz: {data['age']}\nTelefon: {data['phone']}\nEmail: {data['email']}")
    await state.finish()

