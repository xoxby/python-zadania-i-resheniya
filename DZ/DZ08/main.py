import random

matrix = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(random.randint(-20, 10))
    matrix.append(row)

# Выводим матрицу
for row in matrix:
    print(row)

# Считаем отрицательные
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            count = count + 1

print("Количество отрицательных элементов:", count)



import random

matrix = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(random.randint(0, 4))
    matrix.append(row)

for row in matrix:
    print(row)

# Произведение ненулевых
product = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            product = product * matrix[i][j]

print("Произведение ненулевых элементов:", product)

import random

matrix = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(random.randint(0, 10))
    matrix.append(row)

# Одномерный список
replacement = []
for i in range(6):
    replacement.append(random.randint(0, 10))

print("Одномерный список:", replacement)
print("Исходная матрица:")
for row in matrix:
    print(row)

# Заменяем нечётные строки
for i in range(len(matrix)):
    if i % 2 != 0:  
        new_row = []
        for j in range(len(replacement)):
            new_row.append(replacement[j])
        matrix[i] = new_row

print("\nРезультат:")
for row in matrix:
    print(row)