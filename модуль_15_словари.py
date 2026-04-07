# ============================================================
# МОДУЛЬ 15: Словари (dict)
# ============================================================

# --- Задача 1 ---
# Твой код:

me = {"name": "Иван", "age": 20, "city": "Москва", "hobby": "код"}
for k in ("name", "age", "city", "hobby"):
    print(me[k])


# --- Задача 2 ---
# Твой код:

d = {"name": "Иван", "age": 20, "city": "Москва", "hobby": "код"}
print(d)
d["email"] = "ivan@example.com"
print(d)
d["city"] = "СПб"
print(d)
del d["hobby"]
print(d)


# --- Задача 3 ---
# Твой код:

d = {"a": 1, "b": 2}
print(d.get("a"), d.get("c"), d.get("c", "Не найдено"))


# --- Задача 4 ---
# Твой код:

d = {"a": 1, "b": 2, "c": 3}
for k in d.keys():
    print("key", k)
for v in d.values():
    print("val", v)
for k, v in d.items():
    print(k, "->", v)


# --- Задача 5 ---
# Твой код:

months = [1, 2, 3]
names = ["Январь", "Февраль", "Март"]
print(dict(zip(months, names)))


# --- Задача 6 ---
# Твой код:

word = "программирование"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)


# --- Задача 7 ---
# Твой код:

goods = {"1": ["Core-i3", 9, 4500], "2": ["Core-i5", 3, 8500]}
for k, v in goods.items():
    title, qty, price = v
    print(f"{k}) {title} — {qty} шт. по {price} руб.")


# --- Задача 8 ---
# Твой код:

sq = {i: i * i for i in range(1, 11)}
print(sq)


# --- Задача 9 ---
# Твой код:

one = {"apple": 20, "orange": 35}
two = {"pepper": 40, "onion": 55}
merged = {**one, **two}
print(merged)


# --- Задача 10 ---
# Твой код:

n = int(input("Сколько студентов: "))
marks = {}
for _ in range(n):
    nm = input("Имя: ")
    marks[nm] = int(input("Балл: "))
avg = sum(marks.values()) / len(marks)
for nm, sc in marks.items():
    if sc > avg:
        print(nm, sc)


# --- Задача 11 ---
# Твой код:

d = {"a": 1, "b": 2, "c": 3}
inv = {v: k for k, v in d.items()}
print(inv)


# --- Задача 12 ---
# Твой код:

book = {}
while True:
    print("1.Добавить 2.Найти 3.Удалить 4.Все 5.Выход")
    c = input("> ").strip()
    if c == "1":
        nm = input("Имя: ")
        book[nm] = input("Телефон: ")
    elif c == "2":
        nm = input("Имя: ")
        print(book.get(nm, "Нет"))
    elif c == "3":
        book.pop(input("Имя: "), None)
    elif c == "4":
        print(book)
    elif c == "5":
        break
    else:
        print("Нет пункта")
