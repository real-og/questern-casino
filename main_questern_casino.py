from loader import dp
from aiogram import executor
from handlers import *

if __name__ == '__main__':
    print("Starting questern casino bot")
    executor.start_polling(dp, skip_updates=True)