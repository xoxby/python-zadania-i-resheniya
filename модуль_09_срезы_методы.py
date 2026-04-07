# ============================================================
# МОДУЛЬ 9: Срезы и методы списков
# ============================================================

# --- Задача 1 ---
# Твой код:

a = [10, 20, 30, 40, 50, 60, 70]
print(a[:3])
print(a[-2:])
print(a[::2])
print(a[::-1])


# --- Задача 2 ---
# Твой код:

a = [1, 2, 3, 4, 5, 6, 7]
print(a[1:-1])


# --- Задача 3 ---
# Твой код:

s = [5, 9, 3, 7, 1, 8]
s.append(99)
print(s)
s.extend([10, 20])
print(s)
s.insert(2, 100)
print(s)


# --- Задача 4 ---
# Твой код:

s = [5, 9, 3, 7, 1, 8, 3, 9]
s.remove(3)
print(s)
popped = s.pop(2)
print("pop ->", popped)
print(s)


# --- Задача 5 ---
# Твой код:

s = [5, 2, 8, 1, 9, 3, 7]
s.sort()
print(s)
s.sort(reverse=True)
print(s)


# --- Задача 6 ---
# Твой код:

names = ["Дима", "Настя", "Маша", "Яна", "Амин", "Вася"]
names.sort(key=len)
print(names)


# --- Задача 7 ---
# Твой код:

a = [5, 3, 1, 4, 2]
print("до:", a)
b = sorted(a)
print("sorted ->", b, "a:", a)
a.sort()
print("после a.sort():", a)


# --- Задача 8 ---
# Твой код:

a = [1, 2, 3]
b = a
c = a.copy()
a.append(99)
print(b, c)


# --- Задача 9 ---
# Твой код:

n = int(input("Сколько чисел: "))
nums = [int(input()) for _ in range(n)]
nums3 = [x for x in nums if x % 3 == 0]
print(nums3)


# --- Задача 10 ---
# Твой код:

a = [1, 3, 5, 7, 9]
b = [2, 3, 5, 8, 9, 10]
common = [x for x in a if x in b]
print(common)


# --- Задача 11 ---
# Твой код:

x = [4, 7, 2, 9, 1, 5]
m = max(x)
x.remove(m)
x.insert(0, m)
print(x)


# --- Задача 12 ---
# Твой код:

a = [1, 3, 5, 3, 7, 3, 9]
a = [x for x in a if x != 3]
print(a)
