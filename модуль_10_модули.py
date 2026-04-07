# ============================================================
# МОДУЛЬ 10: Модули random, math, time
# ============================================================
import random
import math
import time

# --- Задача 1 ---
# Твой код:

print(random.randint(1, 100))


# --- Задача 2 ---
# Твой код:

nums = [random.randint(0, 50) for _ in range(10)]
print(nums, min(nums), max(nums), sum(nums))


# --- Задача 3 ---
# Твой код:

colors = ["красный", "синий", "зелёный", "жёлтый"]
print(random.choice(colors))


# --- Задача 4 ---
# Твой код:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("до:", nums)
random.shuffle(nums)
print("после:", nums)


# --- Задача 5 ---
# Твой код:

secret = random.randint(1, 50)
tries = 0
while True:
    g = int(input("Угадай 1..50: "))
    tries += 1
    if g < secret:
        print("больше")
    elif g > secret:
        print("меньше")
    else:
        print("Угадал за", tries)
        break


# --- Задача 6 ---
# Твой код:

r = float(input("Радиус: "))
L = 2 * math.pi * r
S = math.pi * r * r
print(f"L={L:.2f}, S={S:.2f}")


# --- Задача 7 ---
# Твой код:

print(math.ceil(7.6), math.floor(7.6), math.sqrt(144))


# --- Задача 8 ---
# Твой код:

print(time.strftime("Сегодня %d %B %Y, %H:%M:%S", time.localtime()))


# --- Задача 9 ---
# Твой код:

sec = int(input("Секунд: "))
print("СТАРТ")
time.sleep(sec)
print("СТОП")


# --- Задача 10 ---
# Твой код:

nums = [random.random() for _ in range(100_000)]
t0 = time.monotonic()
nums.sort()
t1 = time.monotonic()
print(f"{t1 - t0:.4f} сек")
