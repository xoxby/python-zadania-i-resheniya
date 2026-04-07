# ============================================================
# МОДУЛЬ 10: Модули random, math, time
# ============================================================
# Уровень: ★★☆
# Темы: import, from...import, as, random.randint, choice,
#        shuffle, math.sqrt, ceil, floor, pi, time.sleep, strftime
# ============================================================

import random
import math
import time

# --- Задача 1 ---
# Сгенерируй случайное число от 1 до 100. Выведи его.
# import random; random.randint(1, 100)
# Твой код:





print(random.randint(1, 100))

# --- Задача 2 ---
# Создай список из 10 случайных чисел (0-50) через comprehension.
# Выведи список, его min, max и сумму.
# Твой код:





nums = [random.randint(0, 50) for _ in range(10)]
print(nums, min(nums), max(nums), sum(nums))

# --- Задача 3 ---
# Выбери случайный элемент из списка (random.choice).
# colors = ["красный", "синий", "зелёный", "жёлтый"]
# Твой код:





colors = ["красный", "синий", "зелёный", "жёлтый"]
print(random.choice(colors))

# --- Задача 4 ---
# Перемешай список (random.shuffle) и выведи до/после.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Твой код:





nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("до:", nums)
random.shuffle(nums)
print("после:", nums)

# --- Задача 5 ---
# Игра "Угадай число": компьютер загадывает от 1 до 50.
# Пользователь угадывает. Подсказки "больше/меньше". Счётчик попыток.
# Используй random.randint + while.
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
# Посчитай длину окружности и площадь круга по радиусу.
# L = 2 * π * r,  S = π * r²
# Используй math.pi. Выведи с 2 знаками.
# Твой код:





r = float(input("Радиус: "))
L = 2 * math.pi * r
S = math.pi * r * r
print(f"L={L:.2f}, S={S:.2f}")

# --- Задача 7 ---
# Округли число 7.6 вверх (math.ceil) и вниз (math.floor).
# Найди квадратный корень 144 (math.sqrt).
# Твой код:





print(math.ceil(7.6), math.floor(7.6), math.sqrt(144))

# --- Задача 8 ---
# Выведи текущую дату и время красиво:
# "Сегодня 05 апреля 2026, 22:30:00"
# Используй time.strftime().
# Твой код:





print(time.strftime("Сегодня %d %B %Y, %H:%M:%S", time.localtime()))

# --- Задача 9 ---
# Сделай таймер: спроси количество секунд.
# Выведи "СТАРТ", подожди (time.sleep), выведи "СТОП".
# Твой код:





sec = int(input("Секунд: "))
print("СТАРТ")
time.sleep(sec)
print("СТОП")

# --- Задача 10 ---
# Замерь время выполнения: сгенерируй 100000 случайных чисел,
# отсортируй их. Выведи время в секундах.
# Используй time.monotonic() или time.time().
# Твой код:





nums = [random.random() for _ in range(100_000)]
t0 = time.monotonic()
nums.sort()
t1 = time.monotonic()
print(f"{t1 - t0:.4f} сек")
