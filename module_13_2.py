from aiogram import  Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = '7951625578:AAHvt4TkCXKD8RJLp7v4r24cPTl3BvLE36I'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровью!')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
