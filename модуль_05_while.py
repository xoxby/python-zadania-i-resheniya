# ============================================================
# МОДУЛЬ 5: Цикл while
# ============================================================

# --- Задача 1 ---
# Твой код:

i = 1
while i <= 10:
    print(i)
    i += 1


# --- Задача 2 ---
# Твой код:

i = 10
while i >= 1:
    print(i)
    i -= 1


# --- Задача 3 ---
# Твой код:

n = int(input("n: "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(s)


# --- Задача 4 ---
# Твой код:

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# --- Задача 5 ---
# Твой код:

n = int(input("n для факториала: "))
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)


# --- Задача 6 ---
# Твой код:

prod = 1
while True:
    x = int(input("Число (0 — стоп): "))
    if x == 0:
        break
    prod *= x
print("Произведение:", prod)


# --- Задача 7 ---
# Твой код:

i = 0
while i <= 9:
    if i == 3:
        i += 1
        continue
    print(i, end=" ")
    if i == 7:
        break
    i += 1
print()


# --- Задача 8 ---
# Твой код:

secret = 7
tries = 0
while True:
    g = int(input("Угадай (1..10): "))
    tries += 1
    if g < secret:
        print("больше")
    elif g > secret:
        print("меньше")
    else:
        print("Угадал за", tries, "попыток")
        break


# --- Задача 9 ---
# Твой код:

n = int(input("n: "))
d = 1
while d <= n:
    if n % d == 0:
        print(d, end=" ")
    d += 1
print()


# --- Задача 10 ---
# Твой код:

n = int(input("Число: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)


# --- Задача 11 ---
# Твой код:

while True:
    print("1. Привет\n2. Время\n3. Выход")
    c = input("Пункт: ").strip()
    if c == "1":
        print("Привет!")
    elif c == "2":
        print("Сейчас примерно 'пора пить чай'")
    elif c == "3":
        break
    else:
        print("Нет такого пункта")


# --- Задача 12 ---
# Твой код:

total = 0
while True:
    x = int(input("Число (0 — стоп): "))
    if x == 0:
        break
    if x < 0:
        continue
    total += x
print("Сумма положительных:", total)
