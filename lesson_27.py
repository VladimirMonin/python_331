"""
Lesson 27
05.12.2023
Наследование в Python Часть 1
- Понятие родительского класса и дочернего класса
- Когда наследование имеет смысл?
"""


# Класс A - родительский класс
# Инициализатор с принтом + одно поле
class A:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        print(f'Инициализатор класса A'
              f'с атрибутами {self.__dict__}')

    def method_a(self):
        print(f'Метод класса A. Значение поля a = {self.a}')


# Класс B - дочерний класс
class B(A):
    def __init__(self, a: int, c: int, b: int):
        self.c = c
        print(f'Инициализатор класса B'
              f' с атрибутами {self.__dict__}')
        A.__init__(self, a, b)

    def method_b(self):
        print(f'Метод класса B. Значение поля a = {self.a} и b = {self.b}')


# Создаем экземпляр класса A
# a = A(1)
# Создаем экземпляр класса B
b = B(1, 2, 3)

# Проверяем что у нас есть доступ к методу класса A
# a.method_a()
b.method_a()
b.method_b()
