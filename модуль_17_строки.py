# ============================================================
# МОДУЛЬ 17: Строки и методы строк
# ============================================================
import random

# --- Задача 1 ---
# Твой код:

s = "Hello, World! I am learning Python"
print(s.lower(), s.upper(), s.capitalize(), s.title(), s.swapcase(), sep="\n")


# --- Задача 2 ---
# Твой код:

s = "Hello World Hello"
print(s.replace("World", "Python", 1))


# --- Задача 3 ---
# Твой код:

parts = "Иванов Иван Иванович".split()
fam, name, otch = parts
print(fam, name, otch)
print(f"{fam} {name[0]}.{otch[0]}.")


# --- Задача 4 ---
# Твой код:

words = ["Python", "is", "awesome"]
print(" ".join(words))
print("-".join(words))


# --- Задача 5 ---
# Твой код:

s = "I am learning Python programming"
print(s.find("Python"))
print(s.find("Java"))


# --- Задача 6 ---
# Твой код:

s = "Hello World, I love Python"
idx = 0
while True:
    j = s.find("o", idx)
    if j == -1:
        break
    print(j)
    idx = j + 1
print("count:", s.count("o"))


# --- Задача 7 ---
# Твой код:

s = "   Hello, Python!   "
print(s.lstrip())
print(s.rstrip())
print(s.strip())


# --- Задача 8 ---
# Твой код:

for s in ("hello", "123", "hello123", "   ", "Hello World"):
    print(s, s.isalpha(), s.isdigit(), s.isalnum(), s.isspace())


# --- Задача 9 ---
# Твой код:

fio = input("ФИО: ")
print(fio[0].isupper())


# --- Задача 10 ---
# Твой код:

s = "В строке заменить пробелы символом"
print("*".join(s.split()))


# --- Задача 11 ---
# Твой код:

for ch in "AZaz09":
    print(ch, ord(ch))
for code in range(33, 127):
    print(chr(code), end="")
print()


# --- Задача 12 ---
# Твой код:

length = random.randint(8, 12)
pw = "".join(chr(random.randint(33, 126)) for _ in range(length))
print(pw)


# --- Задача 13 ---
# Твой код:

text = input("Текст: ")
words = len(text.split())
sent = text.count(".") + text.count("!") + text.count("?")
print("Слов:", words, "Предложений:", sent)
