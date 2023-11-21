from typing import Dict, Any

simple_set = {
    'Железный человек',
    'Невероятный Халк',
    'Железный человек 2',
    'Тор',
    'Первый мститель',
    'Мстители',
    'Железный человек 3',
    'Тор 2: Царство тьмы',
    'Первый мститель: Другая война',
    'Стражи Галактики',
    'Мстители: Эра Альтрона',
    'Человек-муравей',
    'Первый мститель: Противостояние',
    'Доктор Стрэндж',
    'Стражи Галактики. Часть 2',
    'Человек-паук: Возвращение домой',
    'Тор: Рагнарёк',
    'Чёрная пантера',
    'Мстители: Война бесконечности',
    'Человек-муравей и Оса',
    'Капитан Марвел',
    'Мстители: Финал',
    'Человек-паук: Вдали от дома',
    'Чёрная вдова',
    'Шан-Чи и легенда десяти колец',
    'Вечные',
    'Человек-паук: Нет пути домой',
    'Доктор Стрэндж: В мультивселенной безумия',
    'Тор: Любовь и гром',
    'Чёрная пантера: Ваканда навеки',
    'Человек-муравей и Оса: Квантомания',
    'Стражи Галактики. Часть 3',
    'Капитан Марвел 2',
    'Дэдпул 3',
    'Капитан Америка: Дивный новый мир',
    'Громовержцы',
    'Блэйд',
    'Фантастическая четвёрка',
    'Мстители: Династия Канга',
    'Мстители: Секретные войны',
    'Безымянный фильм о Человеке-пауке',
    'Безымянный фильм о Шан-Чи',
    'Безымянный фильм о Вечных',
    'Безымянный фильм о мутантах'
}

small_dict = {
    'Железный человек': 2008,
    'Невероятный Халк': 2008,
    'Железный человек 2': 2010,
    'Тор': 2011,
    'Первый мститель': 2011,
    'Мстители': 2012,
    'Железный человек 3': 2013,
    'Тор 2: Царство тьмы': 2013,
    'Первый мститель: Другая война': 2014,
    'Стражи Галактики': 2014,
    'Мстители: Эра Альтрона': 2015,
    'Человек-муравей': 2015,
    'Первый мститель: Противостояние': 2016,
    'Доктор Стрэндж': 2016,
    'Стражи Галактики. Часть 2': 2017,
    'Человек-паук: Возвращение домой': 2017,
    'Тор: Рагнарёк': 2017,
    'Чёрная пантера': 2018,
    'Мстители: Война бесконечности': 2018,
    'Человек-муравей и Оса': 2018,
    'Капитан Марвел': 2019,
    'Мстители: Финал': 2019,
    'Человек-паук: Вдали от дома': 2019,
    'Чёрная вдова': 2021,
    'Шан-Чи и легенда десяти колец': 2021,
    'Вечные': 2021,
    'Человек-паук: Нет пути домой': 2021,
    'Доктор Стрэнж: В мультивселенной безумия': 2022,
    'Тор: Любовь и гром': 2022,
    'Чёрная пантера: Ваканда навеки': 2022,
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

full_dict: Dict[int, Dict[str, Any]] = {
    0: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    },

    1: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    },
    2: {
        'title': 'Невероятный Халк',
        'year': 2008,
        'director': 'Луи Летерье',
        'screenwriter': 'Зак Пенн',
        'producer': 'Ави Арад, Гейл Энн Хёрд и Кевин Файги',
        'stage': 'Первая фаза'
    },
    3: {
        'title': 'Железный человек 2',
        'year': 2010,
        'director': 'Джон Фавро',
        'screenwriter': 'Джастин Теру',
        'producer': 'Кевин Файги',
        'stage': 'Первая фаза',
    },
    4: {
        'title': 'Тор',
        'year': 2011,
        'director': 'Кеннет Брана',
        'screenwriter': 'Эшли Эдвард Миллер и Зак Стенц, Дон Пейн',
        'producer': 'Нет данных',
        'stage': 'Первая фаза'
    },
    5: {
        'title': 'Первый мститель',
        'year': 2011,
        'director': 'Джо Джонстон',
        'screenwriter': 'Кристофер Маркус и Стивен Макфили',
        'producer': 'Нет данных',
        'stage': 'Первая фаза'
    },
    6: {
        'title': 'Мстители',
        'year': 2012,
        'director': 'Джосс Уидон',
        'screenwriter': 'Нет данных',
        'producer': 'Нет данных',
        'stage': 'Первая фаза'
    },
    7: {
        'title': 'Железный человек 3',
        'year': 2013,
        'director': 'Шейн Блэк',
        'screenwriter': 'Дрю Пирс и Шейн Блэк',
        'producer': 'Кевин Файги',
        'stage': 'Вторая фаза'
    },
    8: {
        'title': 'Тор 2: Царство тьмы',
        'year': 2013,
        'director': 'Алан Тейлор',
        'screenwriter': 'Кристофер Йост, Кристофер Маркус и Стивен Макфили',
        'producer': 'Нет данных',
        'stage': 'Вторая фаза'
    },
    9: {
        'title': 'Первый мститель: Другая война',
        'year': 2014,
        'director': 'Энтони и Джо Руссо',
        'screenwriter': 'Кристофер Маркус и Стивен Макфили',
        'producer': 'Нет данных',
        'stage': 'Вторая фаза'
    },
    10: {
        'title': 'Стражи Галактики',
        'year': 2014,
        'director': 'Джеймс Ганн',
        'screenwriter': 'Джеймс Ганн и Николь Перлман',
        'producer': 'Нет данных',
        'stage': 'Вторая фаза'
    },
    11: {
        'title': 'Мстители: Эра Альтрона',
        'year': 2015,
        'director': 'Джосс Уидон',
        'screenwriter': 'Нет данных',
        'producer': 'Нет данных',
        'stage': 'Вторая фаза'
    },
    12: {
        'title': 'Человек-муравей',
        'year': 2015,
        'director': 'Пейтон Рид',
        'screenwriter': 'Эдгар Райт и Джо Корниш, Адам Маккей и Пол Радд',
        'producer': 'Кевин Файги и Стивен Бруссар',
        'stage': 'Вторая фаза'
    },
    13: {
        'title': 'Первый мститель: Противостояние',
        'year': 2016,
        'director': 'Энтони и Джо Руссо',
        'screenwriter': 'Кристофер Маркус и Стивен Макфили',
        'producer': 'Кевин Файги',
        'stage': 'Третья фаза'
    },
    14: {
        'title': 'Доктор Стрэндж',
        'year': 2016,
        'director': 'Скотт Дерриксон',
        'screenwriter': 'Джон Спэйтс, Скотт Дерриксон и С. Роберт Каргилл',
        'producer': 'Кевин Файги',
        'stage': 'Третья фаза'
    },
    15: {
        'title': 'Стражи Галактики. Часть 2',
        'year': 2017,
        'director': 'Джеймс Ганн',
        'screenwriter': 'Нет данных',
        'producer': 'Нет данных',
        'stage': 'Третья фаза'
    },
    16: {
        'title': 'Человек-паук: Возвращение домой',
        'year': 2017,
        'director': 'Джон Уоттс',
        'screenwriter': 'Джонатан М. Голдштейн и Джон Френсис Дэйли, Джон Уоттс и Кристофер Форд, Крис МакКенна и Эрик Соммерс',
        'producer': 'Кевин Файги и Эми Паскаль',
        'stage': 'Третья фаза'
    },
    17: {
        'title': 'Тор: Рагнарёк',
        'year': 2017,
        'director': 'Тайка Вайтити',
        'screenwriter': 'Эрик Пирсон, Крэйг Кайл и Кристофер Йост',
        'producer': 'Кевин Файги',
        'stage': 'Третья фаза'
    },
    18: {
        'title': 'Чёрная пантера',
        'year': 2018,
        'director': 'Райан Куглер',
        'screenwriter': 'Райан Куглер и Джо Роберт Коул',
        'producer': 'Нет данных',
        'stage': 'Третья фаза'
    },
    19: {
        'title': 'Мстители: Война бесконечности',
        'year': 2018,
        'director': 'Энтони и Джо Руссо',
        'screenwriter': 'Кристофер Маркус и Стивен Макфили',
        'producer': 'Нет данных',
        'stage': 'Третья фаза'
    },
    20: {
        'title': 'Человек-муравей и Оса',
        'year': 2018,
        'director': 'Пейтон Рид',
        'screenwriter': 'Крис МакКенна и Эрик Соммерс; Пол Радд, Эндрю Баррер и Гэбриел Феррари',
        'producer': 'Кевин Файги и Стивен Бруссар',
        'stage': 'Третья фаза'
    },
    21: {
        'title': 'Капитан Марвел',
        'year': 2019,
        'director': 'Анна Боден и Райан Флек',
        'screenwriter': 'Женева Робертсон-Дуорет, Анна Боден и Райан Флек',
        'producer': 'Кевин Файги',
        'stage': 'Третья фаза'
    },
    22: {
        'title': 'Мстители: Финал',
        'year': 2019,
        'director': 'Энтони и Джо Руссо',
        'screenwriter': 'Кристофер Маркус и Стивен Макфили',
        'producer': 'Нет данных',
        'stage': 'Третья фаза'
    },
    23: {
        'title': 'Человек-паук: Вдали от дома',
        'year': 2019,
        'director': 'Джон Уоттс',
        'screenwriter': 'Крис МакКенна и Эрик Соммерс',
        'producer': 'Кевин Файги и Эми Паскаль',
        'stage': 'Третья фаза'
    },
    24: {
        'title': 'Чёрная вдова',
        'year': 2021,
        'director': 'Кейт Шортланд',
        'screenwriter': 'Эрик Пирсон',
        'producer': 'Кевин Файги',
        'stage': 'Четвёртая фаза'
    },
    25: {
        'title': 'Шан-Чи и легенда десяти колец',
        'year': 2021,
        'director': 'Дестин Дэниэл Креттон',
        'screenwriter': 'Дэвид Каллахэм & Дестин Дэниэл Креттон & Эндрю Лэнем',
        'producer': 'Кевин Файги и Джонатан Шварц',
        'stage': 'Четвёртая фаза'
    },
    26: {
        'title': 'Вечные',
        'year': 2021,
        'director': 'Хлоя Чжао',
        'screenwriter': 'Хлоя Чжао, Хлоя Чжао & Патрик Бёрли и Райан Фирпо & Каз Фирпо',
        'producer': 'Кевин Файги и Нейт Мур',
        'stage': 'Четвёртая фаза'
    },
    27: {
        'title': 'Человек-паук: Нет пути домой',
        'year': 2021,
        'director': 'Джон Уоттс',
        'screenwriter': 'Крис Маккенна & Эрик Соммерс',
        'producer': 'Кевин Файги и Эми Паскаль',
        'stage': 'Четвёртая фаза'
    },
    28: {
        'title': 'Доктор Стрэндж: В мультивселенной безумия',
        'year': 2022,
        'director': 'Сэм Рэйми',
        'screenwriter': 'Майкл Уолдрон',
        'producer': 'Кевин Файги',
        'stage': 'Четвёртая фаза'
    },
    29: {
        'title': 'Тор: Любовь и гром',
        'year': 2022,
        'director': 'Тайка Вайтити',
        'screenwriter': 'Тайка Вайтити и Дженнифер Кейтин Робинсон',
        'producer': 'Кевин Файги и Брэд Уиндербаум',
        'stage': 'Четвёртая фаза'
    },
    30: {
        'title': 'Чёрная пантера: Ваканда навеки',
        'year': 2022,
        'director': 'Райан Куглер',
        'screenwriter': 'Райан Куглер & Джо Роберт Коул',
        'producer': 'Кевин Файги и Нейт Мур',
        'stage': 'Четвёртая фаза'
    },
    31: {
        'title': 'Человек-муравей и Оса: Квантомания',
        'year': 2023,
        'director': 'Пейтон Рид',
        'screenwriter': 'Джефф Лавнесс',
        'producer': 'Кевин Файги и Стивен Бруссар',
        'stage': 'Пятая фаза'
    },
    32: {
        'title': 'Стражи Галактики. Часть 3',
        'year': 2023,
        'director': 'Джеймс Ганн',
        'screenwriter': 'Нет данных',
        'producer': 'Кевин Файги',
        'stage': 'Пятая фаза'
    },
    33: {
        'title': 'Капитан Марвел 2',
        'year': 2023,
        'director': 'Ниа Дакоста',
        'screenwriter': 'Меган Макдоннелл',
        'producer': 'Пост-продакшн',
        'stage': 'Пятая фаза'
    },
    34: {
        'title': 'Дэдпул 3',
        'year': 2024,
        'director': 'Шон Леви',
        'screenwriter': 'Ретт Риз, Пол Верник, Зеб Уэллс и Райан Рейнольдс',
        'producer': 'Кевин Файги, Райан Рейнольдс и Шон Леви',
        'stage': 'Пятая фаза'
    },
    35: {
        'title': 'Капитан Америка: Дивный новый мир',
        'year': 2024,
        'director': 'Джулиус Она',
        'screenwriter': 'Малкольм Спеллман и Далан Массон',
        'producer': 'Кевин Файги и Нейт Мур',
        'stage': 'Пятая фаза'
    },
    36: {
        'title': 'Громовержцы',
        'year': 2024,
        'director': 'Джейк Шрейер',
        'screenwriter': 'Эрик Пирсон',
        'producer': 'Кевин Файги',
        'stage': 'Пятая фаза'
    },
    37: {
        'title': 'Блэйд',
        'year': 2025,
        'director': 'Ян Деманж',
        'screenwriter': 'Майкл Старрбери и Ник Пиццолатто',
        'producer': 'Кевин Файги и Эрик Кэрролл',
        'stage': 'Пятая фаза'
    },
    38: {
        'title': 'Фантастическая четвёрка',
        'year': 2025,
        'director': 'Мэтт Шекман',
        'screenwriter': 'Джефф Каплан, Йен Спрингер и Джош Фридман',
        'producer': 'Кевин Файги',
        'stage': 'Шестая фаза'
    },
    39: {
        'title': 'Мстители: Династия Канга',
        'year': 2026,
        'director': 'Дестин Дэниэл Креттон',
        'screenwriter': 'Джефф Лавнесс',
        'producer': 'Кевин Файги и Джонатан Шварц',
        'stage': 'Шестая фаза'
    },
    40: {
        'title': 'Мстители: Секретные войны',
        'year': 2027,
        'director': 'TBA',
        'screenwriter': 'Майкл Уолдрон',
        'producer': 'Нет данных',
        'stage': 'Шестая фаза'
    },
    41: {
        'title': 'Войны в доспехах',
        'year': 2050,
        'director': 'TBA',
        'screenwriter': 'Яссер Лестер',
        'producer': 'Кевин Файги и Джонатан Шварц',
        'stage': 'Шестая фаза'
    },
    42: {
        'title': 'Баба-Яга и леший',
        'year': 2050,
        'director': 'TBA',
        'screenwriter': 'Яссер Лестер',
        'producer': 'Кевин Файги и Джонатан Шварц',
        'stage': 'Шестая фаза'
    }
}
