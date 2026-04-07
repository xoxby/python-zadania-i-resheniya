# ============================================================
# МОДУЛЬ 3: Логика и условия (if / elif / else)
# ============================================================

# --- Задача 1 ---
# Твой код:

age = int(input("Возраст: "))
print("Доступ разрешён" if age >= 18 else "Доступ запрещён")


# --- Задача 2 ---
# Твой код:

n = float(input("Число: "))
if n > 0:
    print("Положительное")
elif n < 0:
    print("Отрицательное")
else:
    print("Ноль")


# --- Задача 3 ---
# Твой код:

k = int(input("Целое число: "))
print("Чётное" if k % 2 == 0 else "Нечётное")


# --- Задача 4 ---
# Твой код:

a = float(input("a: "))
b = float(input("b: "))
if a == b:
    print("Числа равны")
else:
    print(a if a > b else b)


# --- Задача 5 ---
# Твой код:

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))
m = x
if y > m:
    m = y
if z > m:
    m = z
print("Максимум:", m)


# --- Задача 6 ---
# Твой код:

a = float(input("a: "))
b = float(input("b: "))
op = input("Операция (+,-,*,/): ").strip()
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Ошибка: деление на 0")
    else:
        print(a / b)
else:
    print("Неизвестная операция")


# --- Задача 7 ---
# Твой код:

month = int(input("Номер месяца (1-12): "))
if month in (12, 1, 2):
    print("Зима")
elif month in (3, 4, 5):
    print("Весна")
elif month in (6, 7, 8):
    print("Лето")
elif month in (9, 10, 11):
    print("Осень")
else:
    print("Ошибка")


# --- Задача 8 ---
# Твой код:

a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")


# --- Задача 9 ---
# Твой код:

day = int(input("День недели (1-7): "))
names = {
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "суббота",
    7: "воскресенье",
}
if 1 <= day <= 5:
    print(names[day], "- рабочий день")
elif day in (6, 7):
    print(names[day], "- выходной")
else:
    print("Нет такого дня")


# --- Задача 10 ---
# Твой код:

login = input("Логин: ")
password = input("Пароль: ")
if login == "admin" and password == "1234":
    print("Добро пожаловать!")
else:
    print("Неверные данные")


# --- Задача 11 ---
# Твой код:

a = float(input("a: "))
b = float(input("b: "))
result = "Числа равны" if a == b else (a if a > b else b)
print(result)


# --- Задача 12 ---
# Твой код:

g = int(input("Оценка (1-5): "))
m = {5: "Отлично", 4: "Хорошо", 3: "Удовлетворительно", 2: "Неудовлетворительно", 1: "Ужасно"}
print(m.get(g, "Нет такой оценки"))


# --- Задача 13 ---
# Твой код:

year = int(input("Год: "))
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Високосный" if leap else "Не високосный")


# --- Задача 14 ---
# Твой код:

age = int(input("Возраст: "))
if 0 <= age <= 6:
    print("малыш")
elif 7 <= age <= 12:
    print("ребёнок")
elif 13 <= age <= 17:
    print("подросток")
elif 18 <= age <= 25:
    print("молодой")
elif 26 <= age <= 60:
    print("взрослый")
elif age >= 61:
    print("пожилой")
else:
    print("Ошибка возраста")


# --- Задача 15 ---
# Твой код:

ticket = input("6-значный номер билета: ").strip()
if len(ticket) != 6 or not ticket.isdigit():
    print("Нужно ровно 6 цифр")
else:
    left = sum(int(ch) for ch in ticket[:3])
    right = sum(int(ch) for ch in ticket[3:])
    print("Счастливый" if left == right else "Не счастливый")
