# ============================================================
# МОДУЛЬ 13: Функции — аргументы, *args, **kwargs
# ============================================================

# --- Задача 1 ---
# Твой код:

def line(count=20, symbol="-"):
    print(symbol * count)


line()
line(10)
line(5, "*")
line(symbol="=")


# --- Задача 2 ---
# Твой код:

def power(base, exp=2):
    return base**exp


print(power(3), power(2, 10), power(5, 3))


# --- Задача 3 ---
# Твой код:

def summa(*args):
    return sum(args)


print(summa(1, 2, 3))


# --- Задача 4 ---
# Твой код:

def average(*args):
    return sum(args) / len(args)


print(average(10, 20, 30))


# --- Задача 5 ---
# Твой код:

def intro(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v}")


intro(name="Ivan", age=20, city="Moscow")


# --- Задача 6 ---
# Твой код:

def below_average(*args):
    avg = sum(args) / len(args)
    return [x for x in args if x < avg]


print(below_average(1, 2, 3, 4, 5, 6, 7, 8, 9))


# --- Задача 7 ---
# Твой код:

def print_score(name, *scores):
    print(f"Студент: {name}")
    print("Оценки:", ", ".join(map(str, scores)))


print_score("Ivan", 100, 95, 88)


# --- Задача 8 ---
# Твой код:

def display_info(name, age):
    print(name, age)


display_info("Иван", 20)
display_info(age=20, name="Иван")


# --- Задача 9 ---
# Твой код:

x = 10
print("до:", x)


def func():
    x = 20
    print("внутри (локально):", x)


func()
print("после:", x)


def func2():
    global x
    x = 30


func2()
print("после global:", x)


# --- Задача 10 ---
# Твой код:

def make_counter(city):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(city, count)

    return inner


c1 = make_counter("Москва")
c1()
c1()
