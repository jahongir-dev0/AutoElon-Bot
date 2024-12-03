from typing import Union

from aiogram import Bot
from aiogram import Bot
from aiogram.types import ChatMember
from typing import Union


async def check(user_id: int, channel: Union[int, str]):
    bot = Bot.get_current()
    member: ChatMember = await bot.get_chat_member(user_id=user_id, chat_id=channel)

    # Check if the user is in the chat
    if member.status in ["member", "administrator", "creator"]:
        return True
    return False
