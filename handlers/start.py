from aiogram import Router
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram import F
import aioschedule as schedule
from asyncio import sleep as asyncsleep
from settings import *
from aiogram import types
import random


from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import keyboards

router = Router()


async def send(message: types.Message):
    text = "Вопрос взят из БД"
    # text = readquestions()
    await message.answer(text)


@router.message(Command("start"))  # [2]
# @router.message(commands=["start"])  # [2]
async def cmd_start(message: Message):
    await message.answer(
        welcome_text,
        reply_markup=keyboards.start_kb()
    )


@router.message(Command("test_func"))  # [2]
async def cmd_test_func(message: Message):
    await message.answer(
        "Выбери функции для тестирования",
        reply_markup=keyboards.choose_test_btn_kb()
    )


# Пробуем отправить картинку
@router.message(F.photo)
async def echo_photo_id(message: types.Message):
    """Обработка присланных картинок"""

    print(f'message.photo ')
    print(message.photo)
    print(message.photo[-1].file_id)
    await message.reply(f"получили id изображения {message.photo[-1].file_id}")
    foto_id = message.photo[-1].file_id
    await message.reply_photo(str(foto_id))
    user_id = message.from_user
    # await message.send_photo(user_id, str(foto_id))


    # schedule.every(10).minutes.do(send, message)
    # while True:
    #     await schedule.run_pending()
    #     await asyncsleep(1)


@router.message(Text(text="Справка ❓"))
async def answer_yes(message: Message):
    """Показываем справку при нажатии на соответсвующую кнопку"""
    await message.answer(
        help_instruction_t,
        reply_markup=ReplyKeyboardRemove()
    )


# @router.message(lambda message: is_ForwardedMe(message))
@router.message()
async def handle_forwarded_message(message: types.Message):
    """Обработка пересланного сообщения, прикрепляем кнопки для обработки"""
    text = message.text  # получите текст исходного сообщения, которое было переслано
    print(f'message переслано')
    print(message)
    await message.answer(
        text,
        reply_markup=keyboards.treat_forward_mess_kb()
    )

# Обработка сохранения сообщения

# @router.message(Text(text="нет", text_ignore_case=True))
# async def answer_no(message: Message):
#     await message.answer(
#         "Жаль...",
#         reply_markup=ReplyKeyboardRemove()
#     )

