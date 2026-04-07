# ============================================================
# МОДУЛЬ 8: Списки — основы
# ============================================================

# --- Задача 1 ---
# Твой код:

nums = [3, 7, 1, 9, 5]
print(nums[0], nums[-1], len(nums))


# --- Задача 2 ---
# Твой код:

colors = ["red", "green", "blue", "yellow"]
colors[1] = "orange"
print(colors)


# --- Задача 3 ---
# Твой код:

sq = [i * i for i in range(1, 11)]
print(sq)


# --- Задача 4 ---
# Твой код:

n = int(input("n: "))
arr = []
for _ in range(n):
    arr.append(int(input("число: ")))
print(arr)


# --- Задача 5 ---
# Твой код:

nums = [4, -2, 8, 1, -5, 3, 7]
s = nums[0]
mn = nums[0]
mx = nums[0]
for x in nums[1:]:
    s += x
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print(s, mn, mx)


# --- Задача 6 ---
# Твой код:

nums = list(range(1, 21))
evens = 0
odd_sum = 0
for x in nums:
    if x % 2 == 0:
        evens += 1
    else:
        odd_sum += x
print(evens, odd_sum)


# --- Задача 7 ---
# Твой код:

a = [10, 20, 30, 40, 50]
a[0], a[-1] = a[-1], a[0]
print(a)


# --- Задача 8 ---
# Твой код:

ev = [i for i in range(1, 31) if i % 2 == 0]
print(ev)


# --- Задача 9 ---
# Твой код:

fruits = ["apple", "banana", "cherry"]
f = input("Фрукт: ").strip().lower()
print("Есть" if f in fruits else "Нет")


# --- Задача 10 ---
# Твой код:

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
uniq = []
for x in nums:
    if x not in uniq:
        uniq.append(x)
print(uniq)


# --- Задача 11 ---
# Твой код:

a, b = [1, 2, 3], [4, 5, 6]
print(a + b)
c = a.copy()
c.extend(b)
print(c)
# + создаёт новый список; extend добавляет элементы в существующий


# --- Задача 12 ---
# Твой код:

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b, a == c, a is c)
# == сравнивает содержимое; is сравнивает объекты в памяти
