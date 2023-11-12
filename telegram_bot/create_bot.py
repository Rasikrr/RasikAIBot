import sys

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

sys.path.append("../bardai.py")

from bardai import BardAI

load_dotenv()


bard = BardAI(os.getenv("BARD_API"))
bot = Bot(os.getenv("API_KEY"))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
