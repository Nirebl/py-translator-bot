from loader import dp
from utils.translator import get_translation
from aiogram import types


@dp.message_handler(commands='start')
async def message_check(message: types.Message):
    text = get_translation("Я живой, меня переделали, я стал лучше")
    await message.answer(text)
