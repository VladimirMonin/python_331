
#  📃 Домашнее Задание: Реализация Системы Умного Дома с Использованием ООП и Миксинов в Python

### Краткое Содержание

В рамках этого задания вы создадите систему умного дома, используя принципы объектно-ориентированного программирования
(ООП) и миксинов в Python. Ваша задача — разработать абстрактный класс для умных устройств, ряд наследуемых классов 
для конкретных устройств, а также миксины для расширения их функционала. В конечном итоге вы создадите симуляцию работы
умного дома, демонстрирующую возможности разработанных устройств и миксинов.

### Часть 1: Абстрактный класс и его наследники

1. **Абстрактный класс `Умное устройство`**
   - Атрибуты:
     - `название` (str)
   - Абстрактные методы:
     - `включить()`
     - `выключить()`
     - `получить_состояние()`

2. **Класс `Умная лампочка`** (наследуется от `Умное устройство`)
   - Дополнительные атрибуты:
     - `состояние` (bool)
     - `яркость` (int)
   - Методы:
     - Реализация абстрактных методов родительского класса
     - `регулировать_яркость(значение)`

3. **Класс `Умный датчик дыма`** (наследуется от `Умное устройство`)
   - Дополнительные атрибуты:
     - `состояние` (bool)
   - Методы:
     - Реализация абстрактных методов родительского класса
     - `проверить_дым()`

4. **Класс `Умный увлажнитель воздуха`** (наследуется от `Умное устройство`)
   - Дополнительные атрибуты:
     - `состояние` (bool)
     - `уровень_влажности` (int)
   - Методы:
     - Реализация абстрактных методов родительского класса
     - `установить_влажность(уровень)`

### Часть 2: Миксины

1. **Миксин `Срочное уведомление`**
   - Методы:
     - `отправить_срочное_уведомление(сообщение)`

2. **Миксин `Подключение к Wi-Fi`**
   - Методы:
     - `подключиться_к_wifi(имя_сети, пароль)`

3. **Миксин `Расписание работы`**
   - Атрибуты:
     - `расписание` (dict)
   - Методы:
     - `задать_расписание(расписание)`


### Часть 3: Миксины

Вам необходимо создать классы конкретных устройств. 
Наследуйтесь от класса устройства + нобходимых на ваш взгляд миксинов.
После, проверьте работоспособность устройств.

### Пример Имитации Работы Умного Дома (просто пример)

```python
# Создание и настройка устройств с миксинами
лампочка = УмнаяЛампочкаФилипс("Гостиная")
лампочка.подключиться_к_wifi("Домашний Wi-Fi", "пароль123")
датчик_дыма = УмныйДатчикДымаСяоми("Кухня")
увлажнитель = УмныйУвлажнительБош("Спальня")
увлажнитель.задать_расписание({"08:00": "включить", "23:00": "выключить"})

# Управление устройствами
лампочка.включить()
лампочка.регулировать_яркость(70)
датчик_дыма.включить()
увлажнитель.включить()
увлажнитель.установить_влажность(50)

# Вывод статуса устройств
print(лампочка.получить_состояние())
print(датчик_дыма.получить_состояние())
print(увлажнитель.получить_состояние())

# Симуляция срочного уведомления от датчика дыма
if датчик_дыма.проверить_дым():
    датчик_дыма.отправить_срочное_уведомление("Обнаружен дым на кухне!")
```

# Критерии проверки 👌

1. **Правильность Реализации Абстрактного Класса и Наследников**: Убедитесь, что все абстрактные методы реализованы в подклассах, а наследование выполняется корректно.
2. **Реализация и Интеграция Миксинов**: Проверьте, правильно ли реализованы миксины и интегрированы в классы устройств.
3. **Функциональность Устройств и Миксинов**: Оцените, как устройства и миксины выполняют свои функции (включение/выключение, регулировка параметров, отправка уведомлений и т.д.).
4. **Код и Стиль Программирования**: Проверьте код на соответствие стандартам PEP 8, на чистоту и читаемость.
5. **Симуляция Работы Умного Дома**: Оцените реализацию имитации работы умного дома, включая правильность вывода статусов устройств и реакции на события.
6. Документация классов, методов, аннотации типов.
7. Сдаем в одном файле `py`