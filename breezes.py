"""Работа c ветерками (бризами == вопросы, аффирмации)"""

from typing import Dict, List, NamedTuple
import db
import category


class Breeze(NamedTuple):
    """Структура отзыва"""
    id: int
    text: str
    type_name: str
    type_short_name: str
    type_id: str

    active: str


class Breezes:
    def __init__(self):
        """Инициализируем объект"""
        pass

    def get_items_by_category(self, cat_id: int, active: bool = 1) -> List[Breeze]:
        item_list = db.fetch_where(
            'breezes_category_search, breezes, categories'
            , 'breezes.id breezes.breeze_text reviews.active categories.cat_name categories.short_name categories.id'.split()
            , f'breezes_category_search.id2 = {cat_id} and breezes.id = breezes_category_search.id1'
              f' breezes_category_search.id2 = categories.id'
        )

        ret_list = []
        if item_list:
            return [Breeze(id=item['breezes.id']
                           , text=item['breezes.breeze_text']
                           , type_name=item['categories.cat_name']
                           , type_short_name=item[' categories.short_name']
                           , type_id=item['categories.id']
                           , active=active) if active == item['breezes.active'] else '' for item in item_list]

        return ret_list

    @staticmethod
    def add_breeze(text: str, cat_id: int, owner: Dict = {}):
        # Вставить вопрос или амальгаму и получить его id
        item_id = db.insert("breezes", {
            "breeze_text": text
        })

        # Использовать id отзыва для связи с категорией
        if item_id:
            add_cat_review_id = db.insert("breezes_category_search", {
                "id1": int(item_id),
                "id2": int(cat_id)
            })
            if add_cat_review_id:
                return True
            else:
                return False
        else:
            raise Exception("Не удалось получить id ветерка или добавить ветерок в БД")

    @staticmethod
    def del_breeze(breeze_id: int, cat_id: int):
        # Удалить привязку к БД категорий
        db.delete("categories", breeze_id, f"id1={breeze_id}")
        # Удалить сам отзыв
        db.delete("breezes", breeze_id)
