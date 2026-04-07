# ============================================================
# МОДУЛЬ 7: Вложенные циклы и фигуры
# ============================================================

# --- Задача 1 ---
# Твой код:

for r in range(3):
    for c in range(5):
        print("*", end="")
    print()


# --- Задача 2 ---
# Твой код:

h, w = 4, 6
for r in range(h):
    for c in range(w):
        if r in (0, h - 1) or c in (0, w - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# --- Задача 3 ---
# Твой код:

for r in range(1, 6):
    print("*" * r)


# --- Задача 4 ---
# Твой код:

for r in range(5, 0, -1):
    print("*" * r)


# --- Задача 5 ---
# Твой код:

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}", end="\t")
    print()


# --- Задача 6 ---
# Твой код:

for i in range(8):
    for j in range(8):
        print("#" if (i + j) % 2 == 0 else " ", end="")
    print()


# --- Задача 7 ---
# Твой код:

for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()


# --- Задача 8 ---
# Твой код:

h = 5
for i in range(h):
    spaces = " " * (h - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)


# --- Задача 9 ---
# Твой код:

h = 7
mid = h // 2
for i in range(mid + 1):
    print(" " * (mid - i) + "*" * (2 * i + 1))
for i in range(mid - 1, -1, -1):
    print(" " * (mid - i) + "*" * (2 * i + 1))


# --- Задача 10 ---
# Твой код:

widths = [3, 5, 7]
for w in widths:
    h = (w + 1) // 2
    for i in range(h):
        print(" " * (h - i - 1) + "*" * (2 * i + 1))
    print()
