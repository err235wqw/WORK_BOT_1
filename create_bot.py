from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

token = getenv('TG_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
