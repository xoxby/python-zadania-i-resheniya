# ============================================================
# МОДУЛЬ 17: Строки и методы строк
# ============================================================
# Уровень: ★★☆
# Темы: срезы строк, ord, chr, capitalize, lower, upper, find,
#        replace, split, join, strip, startswith, endswith,
#        isdigit, isalpha, f-строки
# ============================================================

import random

# --- Задача 1 ---
# s = "Hello, World! I am learning Python"
# Выведи: s.lower(), s.upper(), s.capitalize(), s.title(), s.swapcase()
# Твой код:





s = "Hello, World! I am learning Python"
print(s.lower(), s.upper(), s.capitalize(), s.title(), s.swapcase(), sep="\n")

# --- Задача 2 ---
# Замени "World" на "Python" в строке. Используй replace().
# Замени только ПЕРВОЕ вхождение (третий аргумент replace).
# Твой код:





s = "Hello World Hello"
print(s.replace("World", "Python", 1))

# --- Задача 3 ---
# Разбей строку "Иванов Иван Иванович" через split().
# Выведи фамилию, имя и отчество отдельно.
# Собери инициалы: "Иванов И.И."
# Твой код:





parts = "Иванов Иван Иванович".split()
fam, name, otch = parts
print(fam, name, otch)
print(f"{fam} {name[0]}.{otch[0]}.")

# --- Задача 4 ---
# Склей список слов в одну строку через join():
# words = ["Python", "is", "awesome"]  →  "Python is awesome"
# words → "Python-is-awesome"  (через "-")
# Твой код:





words = ["Python", "is", "awesome"]
print(" ".join(words))
print("-".join(words))

# --- Задача 5 ---
# Найди позицию подстроки через find() и index().
# s = "I am learning Python programming"
# Найди "Python". А что если искать "Java"? (find vs index)
# Твой код:





s = "I am learning Python programming"
print(s.find("Python"))
print(s.find("Java"))

# --- Задача 6 ---
# Выведи все позиции символа "o" в строке "Hello World, I love Python".
# count() покажет сколько, а find() в цикле — где каждый.
# Твой код:





s = "Hello World, I love Python"
idx = 0
while True:
    j = s.find("o", idx)
    if j == -1:
        break
    print(j)
    idx = j + 1
print("count:", s.count("o"))

# --- Задача 7 ---
# Используй strip/lstrip/rstrip:
# s = "   Hello, Python!   "
# Удали пробелы слева, справа, с обеих сторон.
# Твой код:





s = "   Hello, Python!   "
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# --- Задача 8 ---
# Проверь строку: содержит ли только буквы? только цифры?
# isalpha(), isdigit(), isalnum(), isspace()
# Протестируй: "hello", "123", "hello123", "   ", "Hello World"
# Твой код:





for s in ("hello", "123", "hello123", "   ", "Hello World"):
    print(s, s.isalpha(), s.isdigit(), s.isalnum(), s.isspace())

# --- Задача 9 ---
# Спроси ФИО. Проверь: начинается ли с заглавной буквы?
# Используй s[0].isupper() или s.istitle().
# Твой код:





fio = input("ФИО: ")
print(fio[0].isupper())

# --- Задача 10 ---
# Замени все пробелы на звёздочки через split() + join():
# "В строке заменить пробелы символом"
# → "В*строке*заменить*пробелы*символом"
# Твой код:





s = "В строке заменить пробелы символом"
print("*".join(s.split()))

# --- Задача 11 ---
# ord() и chr(): выведи ASCII-коды символов "A", "Z", "a", "z", "0", "9".
# Затем выведи все символы от кода 33 до 126.
# Твой код:





for ch in "AZaz09":
    print(ch, ord(ch))
for code in range(33, 127):
    print(chr(code), end="")
print()

# --- Задача 12 ---
# Генератор паролей: создай случайный пароль из 8-12 символов.
# Используй chr(randint(33, 126)) в цикле.
# Твой код:





length = random.randint(8, 12)
pw = "".join(chr(random.randint(33, 126)) for _ in range(length))
print(pw)

# --- Задача 13 ---
# Подсчитай количество слов в строке (через split).
# Подсчитай количество предложений (через count(".") + count("!") + count("?")).
# Текст спроси у пользователя.
# Твой код:





text = input("Текст: ")
words = len(text.split())
sent = text.count(".") + text.count("!") + text.count("?")
print("Слов:", words, "Предложений:", sent)
