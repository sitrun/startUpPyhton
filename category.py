"""Работа c категориями отзывов"""

from typing import Dict, List, NamedTuple
import db


class Category(NamedTuple):
    """Структура категории"""
    id: int
    cat_name: str
    short_name: str
    active: bool


class Categories:
    def __init__(self):
        self._categories = self._load_categories()

    def _load_categories(self) -> List[Category]:
        """Возвращает справочник категорий отзывов из БД"""
        categories = db.fetchall(
            "categories", "id cat_name short_name active".split()
        )
        # categories = self._fill_aliases(categories)
        return categories

    def get_all_categories(self) -> List[Category]:
        """Возвращает справочник категорий отзывов"""
        return self._categories

    def get_cat_by_id(self, cat_id: int) -> Category:
        """Получить по id категории ее название"""
        for cat in self._categories:
            if cat['id'] == cat_id:
                return cat['cat_name']
        return ''
