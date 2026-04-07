# ============================================================
# МОДУЛЬ 11: Двумерные списки (матрицы)
# ============================================================
import random

# --- Задача 1 ---
# Твой код:

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in m:
    print(*row)


# --- Задача 2 ---
# Твой код:

for row in m:
    for x in row:
        print(x, end="\t")
    print()


# --- Задача 3 ---
# Твой код:

mat = [[random.randint(0, 99) for _ in range(5)] for _ in range(4)]
for row in mat:
    print(*row)


# --- Задача 4 ---
# Твой код:

s = 0
for row in mat:
    for x in row:
        s += x
print(s)


# --- Задача 5 ---
# Твой код:

best = mat[0][0]
bi = bj = 0
for i, row in enumerate(mat):
    for j, x in enumerate(row):
        if x > best:
            best, bi, bj = x, i, j
print(best, bi, bj)


# --- Задача 6 ---
# Твой код:

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col0 = [row[0] for row in m]
print(col0)


# --- Задача 7 ---
# Твой код:

m = [[1, 2, 3], [4, 5, 6]]
t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
print(t)


# --- Задача 8 ---
# Твой код:

field = [["-" for _ in range(3)] for _ in range(3)]
field[1][1] = "X"
field[0][0] = "O"
for row in field:
    print(" ".join(row))
