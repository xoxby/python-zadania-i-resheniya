# ============================================================
# МОДУЛЬ 4: Исключения (try / except / else / finally)
# ============================================================

# --- Задача 1 ---
# Твой код:

s = input("Число: ")
try:
    print(int(s))
except ValueError:
    print("Это не число!")


# --- Задача 2 ---
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
# Твой код:

a = input("a: ")
b = input("b: ")
try:
    print(float(a) + float(b))
except ValueError:
    print(a + b)


# --- Задача 6 ---
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
