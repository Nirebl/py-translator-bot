from aiogram import types


async def set_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("kill", "остановить бота"),
    ])
