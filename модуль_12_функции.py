# ============================================================
# МОДУЛЬ 12: Функции — основы
# ============================================================

# --- Задача 1 ---
# Твой код:

def greet(name: str) -> None:
    print(f"Привет, {name}!")


for nm in ("Анна", "Иван", "Олег"):
    greet(nm)


# --- Задача 2 ---
# Твой код:

def get_sum(a, b):
    return a + b


print(get_sum(2, 3))


# --- Задача 3 ---
# Твой код:

def maximum(a, b):
    return a if a > b else b


print(maximum(3, 7))


# --- Задача 4 ---
# Твой код:

def cube(n):
    return n**3


for i in range(1, 11):
    print(i, cube(i))


# --- Задача 5 ---
# Твой код:

def is_even(n):
    return n % 2 == 0


print(is_even(4), is_even(7), is_even(0))


# --- Задача 6 ---
# Твой код:

def area(width, height):
    return width * height


print(area(3, 4))


# --- Задача 7 ---
# Твой код:

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(15)


# --- Задача 8 ---
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
# Твой код:

def count_vowels(text: str) -> int:
    vowels = "аеёиоуыэюя"
    return sum(1 for ch in text.lower() if ch in vowels)


print(count_vowels("Привет"))


# --- Задача 10 ---
# Твой код:

def reverse_string(s: str) -> str:
    out = ""
    for ch in s:
        out = ch + out
    return out


print(reverse_string("python"))
