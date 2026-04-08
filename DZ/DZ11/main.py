# --- Задание 1 ---

tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
s = input("Введите строку для поиска: ")

if s in tpl:
    print("Yes")
else:
    print("No")


# --- Задание 2 ---

data = input("Введите по порядку, без пробелов, элементы кортежа: ")
tpl2 = tuple(data)
print(tpl2)

counted = []  # чтобы не считать повторно
for char in tpl2:
    if char not in counted:
        print(f"Количество {char} = {tpl2.count(char)}")
        counted.append(char)


# --- Задание 3 (дополнительно) ---

winning_numbers = {7, 14, 21, 35, 42}
print("Выигрышные числа:", winning_numbers)

user_num = int(input("Введите число: "))

if user_num in winning_numbers:
    print("Поздравляем, вы угадали!")
else:
    print("Попробуйте еще раз")
