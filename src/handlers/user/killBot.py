from loader import dp
from utils.translator import get_translation
from aiogram import types


@dp.message_handler(commands='kill')
async def message_kill(message: types.Message):
    user = message.from_user.full_name
    text = str(user) + '\n' + get_translation("bot is shutting down")
    await message.answer(text)
    # exit(0)
    from loader import bot
    await bot.close
