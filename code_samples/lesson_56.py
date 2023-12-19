"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
"""
from dataclasses import dataclass


#TODO Практика!
"""
Опишите датакласс для описания книги.
Книга имеет следующие атрибуты:
- Название
- Автор
- Год издания

Создайте 3 экземпляра класса книга.
Создайте список книг.
Сортируйте список книг.
"""