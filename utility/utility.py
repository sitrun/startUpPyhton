"""Вспомогательные функции"""
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def add_reply(markup: ReplyKeyboardBuilder, buttons: list) -> ReplyKeyboardBuilder:
    for button in buttons:
        markup.add(button)
    return markup


def add_inline(markup: InlineKeyboardBuilder, buttons: list) -> InlineKeyboardBuilder:
    for button in buttons:
        markup.add(button)
    return markup
