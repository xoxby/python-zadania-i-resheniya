# ============================================================
# МОДУЛЬ 19: Файлы и модуль os
# ============================================================
import os
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))

# --- Задача 1 ---
# Твой код:

p = os.path.join(BASE, "hello.txt")
with open(p, "w", encoding="utf-8") as f:
    f.write("строка 1\nстрока 2\nстрока 3\n")


# --- Задача 2 ---
# Твой код:

with open(p, "r", encoding="utf-8") as f:
    print(f.read())


# --- Задача 3 ---
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
# Твой код:

with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Строк:", len(lines))


# --- Задача 5 ---
# Твой код:

with open(p, "a", encoding="utf-8") as f:
    f.write("ещё 1\nещё 2\n")
with open(p, "r", encoding="utf-8") as f:
    print(f.read())


# --- Задача 6 ---
# Твой код:

np = os.path.join(BASE, "numbers.txt")
with open(np, "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
with open(np, "r", encoding="utf-8") as f:
    nums = [int(line) for line in f.read().splitlines() if line.strip()]
print(sum(nums))


# --- Задача 7 ---
# Твой код:

cp = os.path.join(BASE, "hello_copy.txt")
with open(p, "r", encoding="utf-8") as f:
    data = f.read().replace("строка", "line")
with open(cp, "w", encoding="utf-8") as f:
    f.write(data)


# --- Задача 8 ---
# Твой код:

with open(p, "r", encoding="utf-8") as f:
    text = f.read()
words = text.split()
print("строк:", text.count("\n") + (1 if text else 0))
print("слов:", len(words))
print("символов:", len(text))


# --- Задача 9 ---
# Твой код:

print(os.getcwd())
print(os.listdir())


# --- Задача 10 ---
# Твой код:

tf = os.path.join(BASE, "test_folder")
os.makedirs(os.path.join(tf, "sub1", "sub2"), exist_ok=True)


# --- Задача 11 ---
# Твой код:

for root, dirs, files in os.walk(tf):
    print(root, dirs, files)


# --- Задача 12 ---
# Твой код:

rp = os.path.join(tf, "report.txt")
with open(rp, "w", encoding="utf-8") as f:
    f.write("report")


# --- Задача 13 ---
# Твой код:

print(os.path.exists(tf), os.path.isdir(tf), os.path.isfile(rp))


# --- Задача 14 ---
# Твой код:

path = r"C:\Users\student\project\main.py"
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))


# --- Задача 15 ---
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
