# ============================================================
# МОДУЛЬ 12: Функции — основы
# ============================================================
# Уровень: ★★☆
# Темы: def, return, параметры, вызов функций
# ============================================================
# --- Задача 1 ---
# Напиши функцию greet(name), которая выводит "Привет, <name>!".
# Вызови её 3 раза с разными именами.
# Твой код:





def greet(name: str) -> None:
    print(f"Привет, {name}!")


for nm in ("Анна", "Иван", "Олег"):
    greet(nm)

# --- Задача 2 ---
# Напиши функцию get_sum(a, b), которая ВОЗВРАЩАЕТ сумму (return).
# Сохрани результат в переменную и выведи.
# Твой код:





def get_sum(a, b):
    return a + b


print(get_sum(2, 3))

# --- Задача 3 ---
# Напиши функцию maximum(a, b), которая возвращает большее число.
# (Без использования max())
# Твой код:





def maximum(a, b):
    return a if a > b else b


print(maximum(3, 7))

# --- Задача 4 ---
# Напиши функцию cube(n), которая возвращает куб числа (n**3).
# Выведи кубы чисел от 1 до 10 через цикл.
# Твой код:





def cube(n):
    return n**3


for i in range(1, 11):
    print(i, cube(i))

# --- Задача 5 ---
# Напиши функцию is_even(n), которая возвращает True/False.
# Протестируй: is_even(4), is_even(7), is_even(0).
# Твой код:





def is_even(n):
    return n % 2 == 0


print(is_even(4), is_even(7), is_even(0))

# --- Задача 6 ---
# Напиши функцию площади прямоугольника area(width, height).
# Вызови с разными аргументами.
# Твой код:





def area(width, height):
    return width * height


print(area(3, 4))

# --- Задача 7 ---
# Напиши функцию fib(n), которая выводит числа Фибоначчи до n.
# Пример: fib(15) → 0 1 1 2 3 5 8 13
# Твой код:





def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(15)

# --- Задача 8 ---
# Напиши функцию check_password(password), которая проверяет:
# - длина >= 8 символов
# - есть хотя бы одна заглавная буква
# - есть хотя бы одна цифра
# Возвращает True/False + печатает что именно не так.
# Твой код:





def check_password(password: str) -> bool:
    ok_len = len(password) >= 8
    up = any("A" <= ch <= "Z" for ch in password)
    low = any("a" <= ch <= "z" for ch in password)
    dig = any(ch.isdigit() for ch in password)
    if not ok_len:
        print("Короткий пароль")
    if not up:
        print("Нет заглавной")
    if not low:
        print("Нет строчной")
    if not dig:
        print("Нет цифры")
    return ok_len and up and low and dig


print(check_password("Abcdefg1"))

# --- Задача 9 ---
# Напиши функцию count_vowels(text), которая возвращает
# количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в тексте.
# Твой код:





def count_vowels(text: str) -> int:
    vowels = "аеёиоуыэюя"
    return sum(1 for ch in text.lower() if ch in vowels)


print(count_vowels("Привет"))

# --- Задача 10 ---
# Напиши функцию reverse_string(s), которая возвращает строку наоборот.
# Не используй [::-1] — только цикл.
# Твой код:





def reverse_string(s: str) -> str:
    out = ""
    for ch in s:
        out = ch + out
    return out


print(reverse_string("python"))
