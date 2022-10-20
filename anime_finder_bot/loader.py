from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.db_anime_users import db
from data import config

# Create bot variable
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# create a storage
storage = MemoryStorage()

# create a dispatcher
dp: Dispatcher = Dispatcher(bot=bot, storage=storage)

__all__ = ['bot', 'dp', 'db']
