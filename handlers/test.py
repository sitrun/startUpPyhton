from loader import *
from aiogram import Router

from aiogram.filters.text import Text
from aiogram import F
import aioschedule as schedule
from asyncio import sleep as asyncsleep
from settings import *

import random

from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import keyboards

router = Router()


@router.callback_query(F.data.startswith("test_btn"))
async def test_command(cd: types.CallbackQuery):
    """Показать другие категории по кнопке"""
    command = cd.data.split(":")[1]
    await cd.message.edit_text(
        f"Кнопка отпработала с командой {command}"
     )

