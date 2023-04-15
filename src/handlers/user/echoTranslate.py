from utils.translator import get_translation
from loader import dp
from aiogram import types


@dp.message_handler()
async def any_text_message(message: types.Message):
    user = message.from_user
    message_id = message.message_id
    text = str(user.full_name) + " said: \n" + get_translation(message.text)

    await message.answer(text, reply=message_id)
