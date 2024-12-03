import re

from aiogram.types import ContentType, ContentTypes
from loader import dp
from aiogram import types


# @dp.message_handler(commands=['help', 'start', 'boshlash'])
# async def filter_text(message: types.Message):
#     await message.answer("Siz komanda ishlatdingiz!!")


@dp.message_handler(content_types=ContentTypes.VOICE)
async def filter_text(message: types.Message):
    await message.answer("Ovozingdan!!!")


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def filter_text(message: types.Message):
    await message.answer("chiroyli rasm!!!")


@dp.message_handler(lambda message: "salom" in message.text)
async def filter_text(message: types.Message):
    await message.answer("salom sozi topildi!!!")


@dp.message_handler(lambda message: "salom" == message.text)
async def filter_text(message: types.Message):
    await message.answer("salom dedingiz!!!")


@dp.message_handler(regexp=re.compile(r'\+d$', re.IGNORECASE))
async def filter_text(message: types.Message):
    await message.answer("raqamlar!")
