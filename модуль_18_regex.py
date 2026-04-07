# ============================================================
# МОДУЛЬ 18: Регулярные выражения (regex)
# ============================================================
import re

# --- Задача 1 ---
# Твой код:

s = "В 2026 году я прошёл 15 уроков и решил 200 задач"
print(re.findall(r"\d+", s))


# --- Задача 2 ---
# Твой код:

s = "Hello, World! I am 20 years old."
print(re.findall(r"\w+", s))


# --- Задача 3 ---
# Твой код:

s = "один   два     три  четыре"
print(re.sub(r"\s+", "-", s))


# --- Задача 4 ---
# Твой код:

def ok_login(name: str) -> bool:
    return bool(re.fullmatch(r"[\w-]{3,16}", name))


for x in ("Python_master", "@invalid", "ab", "valid-user-123"):
    print(x, ok_login(x))


# --- Задача 5 ---
# Твой код:

text = "Пишите на ivan@gmail.com или anna@mail.ru для связи"
print(re.findall(r"[a-z._-]+@[a-z._-]+", text))


# --- Задача 6 ---
# Твой код:

text = "Родился 05-03-1987, женился 15.06.2015"
print(re.findall(r"\d{2}[.-]\d{2}[.-]\d{4}", text))


# --- Задача 7 ---
# Твой код:

text = "Текст [1] и ещё [важно] и [16][17]"
print(re.findall(r"\[.*?\]", text))


# --- Задача 8 ---
# Твой код:

s = "one,two;three,four;five"
print(re.split(r"[,;]", s))


# --- Задача 9 ---
# Твой код:

text = "Python, python, PYTHON — всё один язык"
print(re.findall(r"python", text, flags=re.I))


# --- Задача 10 ---
# Твой код:

text = "+7 499 456-45-78, +74994564578, 7(499) 456 45 78"
phones = []
for chunk in text.split(","):
    digits = re.sub(r"\D", "", chunk)
    if len(digits) == 11 and digits.startswith("7"):
        phones.append("+" + digits)
print(phones)


# --- Задача 11 ---
# Твой код:

html = "<p>Текст <b>жирный</b> и <i>курсив</i></p>"
print(re.sub(r"<.*?>", "", html))


# --- Задача 12 ---
# Твой код:

url = "https://www.python.org/docs"
print(url.split("//", 1)[1].split("/", 1)[0])
