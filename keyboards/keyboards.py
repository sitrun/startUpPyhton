from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from utility import utility


def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Справка ❓")
    kb.button(text="Получить осознание 🌿")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def treat_forward_mess_kb() -> ReplyKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.button(text="Сохранить в БД ☑️")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choose_test_btn_kb() -> InlineKeyboardMarkup:
    """Кнопки для тестирования функций бота"""
    buttons = [
        InlineKeyboardButton(text=f"Записать в БД один бриз", callback_data="test_btn:record_breeze"),
        InlineKeyboardButton(text=f"Записать Бриз с категорией", callback_data="test_btn:record_breeze_cat"),
        InlineKeyboardButton(text=f"Показать все записи из БД", callback_data="test_btn:show_breezes"),
        InlineKeyboardButton(text=f"Показать все записи из БД с категориями", callback_data="test_btn:show_breezes_w_cats")
    ]

    markup = utility.add_inline(InlineKeyboardBuilder(), buttons)
    markup.adjust(1, 2)
    return InlineKeyboardMarkup(inline_keyboard=markup.export())
