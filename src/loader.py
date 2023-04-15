from aiogram import Bot, Dispatcher
from utils.getBotToken import getToken

bot = Bot(token=getToken())
dp = Dispatcher(bot)
