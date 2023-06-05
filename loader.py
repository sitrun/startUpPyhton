import aioredis
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from states import *
from settings import *
from keyboards.keyboards import *

import sys
import os
import asyncio

TG_AIOGRAM_TOKEN = os.environ['BOT_TOKEN']
bot: Bot = Bot(token=TG_AIOGRAM_TOKEN, parse_mode="HTML")
# dp: Dispatcher = Dispatcher()


