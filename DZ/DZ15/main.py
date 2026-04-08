
# --- Задание 1 ---

product = lambda x, y, z: x * y * z

print(product(2, 5, 5))  # 50


# --- Задание 2 ---
students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]


sorted_by_name = sorted(students, key=lambda s: s['name'])
print(sorted_by_name)


sorted_by_final = sorted(students, key=lambda s: s['final'], reverse=True)
print(sorted_by_final)


# --- Задание 3 ---

students2 = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

max_student = max(students2, key=lambda s: s['final'])
min_student = min(students2, key=lambda s: s['final'])

print(max_student)
print(min_student)


# --- Задание 4 ---

nums = [3, 5, 7, 3, 9, 5, 7, 2]

squares = list(map(lambda x: x ** 2, nums))
cubes = list(map(lambda x: x ** 3, nums))

print(squares)  # [9, 25, 49, 9, 81, 25, 49, 4]
print(cubes)    # [27, 125, 343, 27, 729, 125, 343, 8]
