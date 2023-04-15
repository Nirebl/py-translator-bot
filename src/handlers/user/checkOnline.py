from loader import dp
from utils.translator import get_translation
from aiogram import types


@dp.message_handler(commands='check')
async def message_check(message: types.Message):
    text = get_translation("bot is online")
    await message.answer(text)
