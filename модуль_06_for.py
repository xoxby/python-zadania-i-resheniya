# ============================================================
# МОДУЛЬ 6: Цикл for и range()
# ============================================================

# --- Задача 1 ---
# Твой код:

for i in range(1, 11):
    print(i)


# --- Задача 2 ---
# Твой код:

for i in range(2, 21, 2):
    print(i)


# --- Задача 3 ---
# Твой код:

for i in range(10, 0, -1):
    print(i)


# --- Задача 4 ---
# Твой код:

n = int(input("n: "))
s = 0
for i in range(1, n + 1):
    s += i * i
print(s)


# --- Задача 5 ---
# Твой код:

n = int(input("n: "))
for d in range(1, n + 1):
    if n % d == 0:
        print(d, end=" ")
print()


# --- Задача 6 ---
# Твой код:

k = int(input("Таблица для числа: "))
for i in range(1, 11):
    print(f"{k} x {i} = {k * i}")


# --- Задача 7 ---
# Твой код:

s = input("Строка: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


# --- Задача 8 ---
# Твой код:

vowels = "аеёиоуыэюя"
s = input("Строка: ").lower()
cnt = 0
for ch in s:
    if ch in vowels:
        cnt += 1
print(cnt)


# --- Задача 9 ---
# Твой код:

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


# --- Задача 10 ---
# Твой код:

n = int(input("Проверка на простоту, n>=2: "))
for d in range(2, n):
    if n % d == 0:
        print("Не простое")
        break
else:
    print("Простое")


# --- Задача 11 ---
# Твой код:

for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# --- Задача 12 ---
# Твой код:

for x in range(100, 1000):
    a, b, c = x // 100, (x // 10) % 10, x % 10
    if a + b + c == 10:
        print(x, end=" ")
print()
