# ============================================================
# МОДУЛЬ 16: lambda, map, filter
# ============================================================

# --- Задача 1 ---
# Твой код:

double = lambda x: x * 2
print(double(5))
print(double("abc"))


# --- Задача 2 ---
# Твой код:

nums = [1, 2, 3, 4, 5]
print(list(map(lambda t: t * 2, nums)))


# --- Задача 3 ---
# Твой код:

strings = ["1", "2", "3", "4", "5"]
print(list(map(int, strings)))


# --- Задача 4 ---
# Твой код:

nums = [55, 77, 32, 89, 94, 45, 22, 99, 26]
print(list(filter(lambda x: x > 50, nums)))


# --- Задача 5 ---
# Твой код:

words = ("abc", "abcd", "def", "tres", "ufo", "lopp")
print(list(filter(lambda s: len(s) == 4, words)))


# --- Задача 6 ---
# Твой код:

players = [
    {"name": "Антон", "rating": 9},
    {"name": "Алексей", "rating": 10},
    {"name": "Фёдор", "rating": 4},
]
print(sorted(players, key=lambda p: p["rating"], reverse=True))


# --- Задача 7 ---
# Твой код:

d = {"b": 10, "a": 15, "c": 32}
print(sorted(d.items(), key=lambda kv: kv[1]))


# --- Задача 8 ---
# Твой код:

a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))


# --- Задача 9 ---
# Твой код:

days = {
    1: lambda: "Понедельник",
    2: lambda: "Вторник",
    3: lambda: "Среда",
    4: lambda: "Четверг",
    5: lambda: "Пятница",
    6: lambda: "Суббота",
    7: lambda: "Воскресенье",
}
k = int(input("День 1-7: "))
print(days[k]())


# --- Задача 10 ---
# Твой код:

def stars(fn):
    def wrap():
        print("*" * 40)
        fn()
        print("=" * 40)

    return wrap


@stars
def hello():
    print("Hello World!")


hello()


# --- Задача 11 ---
# Твой код:

def count_calls(fn):
    n = 0

    def wrap(*a, **kw):
        nonlocal n
        n += 1
        print(f"Вызов функции #{n}")
        return fn(*a, **kw)

    return wrap


@count_calls
def f():
    print("work")


f()
f()
