# ============================================================
# МОДУЛЬ 20: Рекурсия
# ============================================================

# --- Задача 1 ---
# Твой код:

def countdown(n):
    if n < 0:
        return
    print(n, end=" ")
    countdown(n - 1)


countdown(5)
print()


# --- Задача 2 ---
# Твой код:

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# --- Задача 3 ---
# Твой код:

def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_list(lst[1:])


print(sum_list([1, 3, 5, 7, 9]))


# --- Задача 4 ---
# Твой код:

def to_str(n, base):
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]
    return to_str(n // base, base) + convert[n % base]


print(to_str(255, 16), to_str(10, 2))


# --- Задача 5 ---
# Твой код:

def count_nested(item_list):
    cnt = 0
    for item in item_list:
        if isinstance(item, list):
            cnt += count_nested(item)
        else:
            cnt += 1
    return cnt


names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard"], "Alex", ["Bea", "Bill"], "Ann"]
print(count_nested(names))


# --- Задача 6 ---
# Твой код:

def remove_spaces(s):
    if not s:
        return ""
    if s[0] in " \t":
        return remove_spaces(s[1:])
    return s[0] + remove_spaces(s[1:])


print(remove_spaces("  Hello\tWorld  "))


# --- Задача 7 ---
# Твой код:

def elevator(n):
    if n == 0:
        print("Вы в подвале")
        return
    print("=>", n)
    elevator(n - 1)
    print(n, end=" ")


elevator(5)
print()


# --- Задача 8 ---
# Твой код:

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(11)])


# --- Задача 9 ---
# Твой код:

def binary_search(lst, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if lst[mid] == target:
        return True
    if lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    return binary_search(lst, target, low, mid - 1)


a = [1, 3, 5, 7, 9, 11]
print(binary_search(a, 7, 0, len(a) - 1))


# --- Задача 10 ---
# Твой код:

def flatten(x):
    out = []
    for item in x:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out


print(flatten([1, [2, [3, 4], 5], [6, 7]]))
