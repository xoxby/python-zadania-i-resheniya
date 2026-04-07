# ============================================================
# МОДУЛЬ 19: Файлы и модуль os
# ============================================================
# Уровень: ★★★
# Темы: open, read, readline, readlines, write, writelines,
#        with open, tell, seek, os.getcwd, os.listdir, os.mkdir,
#        os.makedirs, os.remove, os.rename, os.walk, os.path.join
# ============================================================
import os
import os.path


BASE = os.path.dirname(os.path.abspath(__file__))

# --- РАБОТА С ФАЙЛАМИ ---


# --- Задача 1 ---
# Создай файл "hello.txt" и запиши в него 3 строки текста.
# Используй with open("hello.txt", "w") as f: f.write(...)
# Твой код:





p = os.path.join(BASE, "hello.txt")
with open(p, "w", encoding="utf-8") as f:
    f.write("строка 1\nстрока 2\nстрока 3\n")

# --- Задача 2 ---
# Прочитай файл "hello.txt" целиком через read().
# Выведи содержимое.
# Твой код:





with open(p, "r", encoding="utf-8") as f:
    print(f.read())

# --- Задача 3 ---
# Прочитай файл "hello.txt" построчно через readline() в цикле.
# Выведи каждую строку с номером.
# Твой код:





with open(p, "r", encoding="utf-8") as f:
    i = 1
    while True:
        line = f.readline()
        if not line:
            break
        print(i, line.rstrip())
        i += 1

# --- Задача 4 ---
# Прочитай файл через readlines(). Выведи количество строк.
# Твой код:





with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Строк:", len(lines))

# --- Задача 5 ---
# Допиши в файл "hello.txt" ещё 2 строки (mode = "a").
# Затем прочитай файл и убедись, что всё добавилось.
# Твой код:





with open(p, "a", encoding="utf-8") as f:
    f.write("ещё 1\nещё 2\n")
with open(p, "r", encoding="utf-8") as f:
    print(f.read())

# --- Задача 6 ---
# Создай файл "numbers.txt". Запиши в него числа от 1 до 10 (каждое на новой строке).
# Затем прочитай, преобразуй в список int и выведи сумму.
# Твой код:





np = os.path.join(BASE, "numbers.txt")
with open(np, "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
with open(np, "r", encoding="utf-8") as f:
    nums = [int(line) for line in f.read().splitlines() if line.strip()]
print(sum(nums))

# --- Задача 7 ---
# Скопируй файл: прочитай "hello.txt", запиши в "hello_copy.txt".
# При копировании замени слово по выбору (например "строка" → "line").
# Используй replace() при записи.
# Твой код:





cp = os.path.join(BASE, "hello_copy.txt")
with open(p, "r", encoding="utf-8") as f:
    data = f.read().replace("строка", "line")
with open(cp, "w", encoding="utf-8") as f:
    f.write(data)

# --- Задача 8 ---
# Подсчитай в файле количество строк, слов и символов.
# Используй split() для подсчёта слов.
# Твой код:





with open(p, "r", encoding="utf-8") as f:
    text = f.read()
words = text.split()
print("строк:", text.count("\n") + (1 if text else 0))
print("слов:", len(words))
print("символов:", len(text))

# --- МОДУЛЬ OS ---

# --- Задача 9 ---
# Выведи текущую директорию (os.getcwd()).
# Выведи список файлов в текущей директории (os.listdir()).
# Твой код:





print(os.getcwd())
print(os.listdir())

# --- Задача 10 ---
# Создай папку "test_folder" (os.mkdir).
# Внутри создай вложенные папки "test_folder/sub1/sub2" (os.makedirs).
# Твой код:





tf = os.path.join(BASE, "test_folder")
os.makedirs(os.path.join(tf, "sub1", "sub2"), exist_ok=True)

# --- Задача 11 ---
# Обойди папку "test_folder" через os.walk().
# Для каждой папки выведи: корень, подпапки, файлы.
# Твой код:





for root, dirs, files in os.walk(tf):
    print(root, dirs, files)

# --- Задача 12 ---
# Создай файл внутри "test_folder/report.txt" с текстом.
# Используй os.path.join("test_folder", "report.txt") для пути.
# Твой код:





rp = os.path.join(tf, "report.txt")
with open(rp, "w", encoding="utf-8") as f:
    f.write("report")

# --- Задача 13 ---
# Проверь: существует ли файл? Является ли путь папкой?
# os.path.exists("test_folder")
# os.path.isdir("test_folder")
# os.path.isfile("test_folder/report.txt")
# Твой код:





print(os.path.exists(tf), os.path.isdir(tf), os.path.isfile(rp))

# --- Задача 14 ---
# Разбери путь на части:
# path = r"C:\Users\student\project\main.py"
# os.path.dirname(path)  →  директория
# os.path.basename(path) →  имя файла
# os.path.split(path)    →  (директория, файл)
# Твой код:





path = r"C:\Users\student\project\main.py"
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))

# --- Задача 15 ---
# Удали файл "test_folder/report.txt" (os.remove).
# Удали пустые папки (os.rmdir).
# Напиши функцию, которая рекурсивно удаляет папку со всем содержимым.
# Твой код:





def rm_tree(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
        return
    for name in os.listdir(path):
        rm_tree(os.path.join(path, name))
    os.rmdir(path)


rm_tree(tf)
