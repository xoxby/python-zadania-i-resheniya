# ============================================================
# МОДУЛЬ 4: Исключения (try / except / else / finally)
# ============================================================
# Уровень: ★★☆
# Темы: try, except, else, finally, ValueError, ZeroDivisionError
# ============================================================
# --- Задача 1 ---
# Спроси число через input(). Оберни int() в try/except.
# При ошибке выведи "Это не число!".
# Твой код:





s = input("Число: ")
try:
    print(int(s))
except ValueError:
    print("Это не число!")

# --- Задача 2 ---
# Спроси два числа, раздели первое на второе.
# Обработай ValueError И ZeroDivisionError отдельными except.
# Твой код:





try:
    a = float(input("a: "))
    b = float(input("b: "))
    print(a / b)
except ValueError:
    print("Некорректный ввод")
except ZeroDivisionError:
    print("Деление на ноль")

# --- Задача 3 ---
# Как задача 2, но добавь else (выводит "Всё ок") и finally ("Конец").
# Твой код:





try:
    a = float(input("a: "))
    b = float(input("b: "))
    print(a / b)
except ValueError:
    print("Некорректный ввод")
except ZeroDivisionError:
    print("Деление на ноль")
else:
    print("Всё ок")
finally:
    print("Конец")

# --- Задача 4 ---
# Проси пользователя вводить число, пока не введёт корректное.
# Используй while True + try/except + break.
# Твой код:





while True:
    s = input("Введите целое число: ")
    try:
        n = int(s)
        print("Ок:", n)
        break
    except ValueError:
        print("Попробуйте ещё раз")

# --- Задача 5 ---
# Спроси два значения: a и b.
# Если оба — числа → выведи a + b как числа.
# Если хотя бы одно не число → выведи a + b как строки.
# Используй try/except.
# Твой код:





a = input("a: ")
b = input("b: ")
try:
    print(float(a) + float(b))
except ValueError:
    print(a + b)

# --- Задача 6 ---
# Напиши функцию safe_divide(a, b), которая:
# - возвращает a / b если b != 0
# - возвращает "Деление на ноль!" если b == 0
# - ловит TypeError если передали не числа
# Протестируй: safe_divide(10, 2), safe_divide(10, 0), safe_divide("a", 2)
# Твой код:





def safe_divide(a, b):
    try:
        if b == 0:
            return "Деление на ноль!"
        return a / b
    except TypeError:
        return "Нужны числа"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("a", 2))

# --- Задача 7 ---
# "Калькулятор с защитой": цикл, в котором:
# 1. Спроси два числа (с защитой от ошибок ввода)
# 2. Спроси операцию (+, -, *, /)
# 3. Выведи результат (с защитой от деления на 0)
# 4. Спроси "Ещё? (да/нет)" — если "нет", выходи
# Твой код:





while True:
    try:
        a = float(input("Число a: "))
        b = float(input("Число b: "))
    except ValueError:
        print("Введите числа")
        continue
    op = input("Операция (+,-,*,/): ").strip()
    try:
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a / b if b != 0 else "Деление на 0")
        else:
            print("Неизвестная операция")
    except ZeroDivisionError:
        print("Деление на 0")
    ans = input("Ещё? (да/нет): ").strip().lower()
    if ans != "да":
        break
