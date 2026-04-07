# ============================================================
# МОДУЛЬ 14: Кортежи и множества
# ============================================================

# --- Задача 1 ---
# Твой код:

t = (1, 2, 3, 4, 5)
print(t[0], t[-1], len(t))
try:
    t[0] = 9
except TypeError as e:
    print("Нельзя менять кортеж:", e)


# --- Задача 2 ---
# Твой код:

t = ("Иван", 20, "Москва")
name, age, city = t
print(name, age, city)


# --- Задача 3 ---
# Твой код:

def stats(lst):
    s = sum(lst)
    return min(lst), max(lst), s / len(lst)


mn, mx, av = stats([1, 2, 3, 4])
print(mn, mx, av)


# --- Задача 4 ---
# Твой код:

t = tuple(2**i for i in range(13))
print(t)


# --- Задача 5 ---
# Твой код:

lst = [1, 2, 3, 4, 5]
print(type(lst), lst)
tpl = tuple(lst)
print(type(tpl), tpl)
lst2 = list(tpl)
print(type(lst2), lst2)


# --- Задача 6 ---
# Твой код:

nums = [1, 3, 3, 5, 5, 5, 7, 7, 9]
st = set(nums)
print(st, len(st))


# --- Задача 7 ---
# Твой код:

s1, s2 = "Hello", "World"
print(set(s1.lower()) & set(s2.lower()))


# --- Задача 8 ---
# Твой код:

drawing = {"Марина", "Женя", "Света"}
music = {"Костя", "Женя", "Илья"}
print("Оба:", drawing & music)
print("Только рисование:", drawing - music)
print("Только музыка:", music - drawing)


# --- Задача 9 ---
# Твой код:

a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
out = []
for x in a:
    if x not in out:
        out.append(x)
print(out)


# --- Задача 10 ---
# Твой код:

A, B = {1, 2}, {1, 2, 3, 4, 5}
print(A.issubset(B))


# --- Задача 11 ---
# Твой код:

fs = frozenset({1, 2, 3})
try:
    fs.add(4)
except AttributeError as e:
    print("frozenset неизменяем:", e)
# frozenset нужен как ключ dict/элемент set и для хэшируемых коллекций
