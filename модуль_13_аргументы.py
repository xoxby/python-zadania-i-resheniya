# ============================================================
# МОДУЛЬ 13: Функции — аргументы, *args, **kwargs
# ============================================================
# Уровень: ★★★
# Темы: значения по умолчанию, именованные аргументы,
#        *args, **kwargs, области видимости (global, nonlocal)
# ============================================================
# --- Задача 1 ---
# Напиши функцию line(count=20, symbol="-"), которая печатает линию.
# Вызови: line(), line(10), line(5, "*"), line(symbol="=").
# Твой код:





def line(count=20, symbol="-"):
    print(symbol * count)


line()
line(10)
line(5, "*")
line(symbol="=")

# --- Задача 2 ---
# Напиши функцию power(base, exp=2), которая возвращает base**exp.
# Протестируй: power(3), power(2, 10), power(5, 3).
# Твой код:





def power(base, exp=2):
    return base**exp


print(power(3), power(2, 10), power(5, 3))

# --- Задача 3 ---
# Напиши функцию summa(*args), которая возвращает сумму ВСЕХ аргументов.
# summa(1, 2, 3) → 6, summa(10, 20, 30, 40) → 100
# Твой код:





def summa(*args):
    return sum(args)


print(summa(1, 2, 3))

# --- Задача 4 ---
# Напиши функцию average(*args), которая возвращает среднее.
# average(10, 20, 30) → 20.0
# Твой код:





def average(*args):
    return sum(args) / len(args)


print(average(10, 20, 30))

# --- Задача 5 ---
# Напиши функцию intro(**kwargs), которая печатает все переданные данные:
# intro(name="Ivan", age=20, city="Moscow")
# Вывод: "name is Ivan", "age is 20", "city is Moscow"
# Твой код:





def intro(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v}")


intro(name="Ivan", age=20, city="Moscow")

# --- Задача 6 ---
# Напиши функцию below_average(*args), которая возвращает
# список чисел, которые НИЖЕ среднего.
# below_average(1, 2, 3, 4, 5, 6, 7, 8, 9) → [1, 2, 3, 4]
# Твой код:





def below_average(*args):
    avg = sum(args) / len(args)
    return [x for x in args if x < avg]


print(below_average(1, 2, 3, 4, 5, 6, 7, 8, 9))

# --- Задача 7 ---
# Напиши функцию print_score(name, *scores), которая выводит:
# "Студент: Ivan"
# "Оценки: 100, 95, 88"
# Твой код:





def print_score(name, *scores):
    print(f"Студент: {name}")
    print("Оценки:", ", ".join(map(str, scores)))


print_score("Ivan", 100, 95, 88)

# --- Задача 8 ---
# Напиши функцию display_info(name, age), вызови её:
# а) позиционно: display_info("Иван", 20)
# б) по имени: display_info(age=20, name="Иван")
# Убедись, что результат одинаковый.
# Твой код:





def display_info(name, age):
    print(name, age)


display_info("Иван", 20)
display_info(age=20, name="Иван")

# --- Задача 9 ---
# Покажи области видимости:
# x = 10 (глобальная)
# def func(): x = 20 (локальная)
# Выведи x до, внутри и после вызова функции.
# Затем попробуй с global x — что изменится?
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
# Напиши функцию counter(city), которая считает вызовы:
# Каждый вызов counter("Москва") увеличивает счётчик.
# Используй замыкание (closure): внешняя функция создаёт переменную,
# внутренняя её увеличивает через nonlocal.
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
