from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

storage = MemoryStorage()

load_dotenv()
sub_channel_id = getenv('SUB_CHANNEL')
token = getenv('TG_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
