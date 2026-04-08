cel = 42

print("Я загадал число от 1 до 100.")
print("Попробуй угадать!")
print("Если надоело - введи 0.")

popitki = 0

while True:
    try:
        chislo = int(input("Введите число: "))
    except ValueError:
        print("Неправильный ввод! Нужно целое число.")
        continue
    if chislo == 0:
        print("Вы вышли из игры.")
        break

    popitki = popitki + 1

    if chislo == cel:
        print("Вы угадали загаданное число с", popitki, "раза")
        break
    elif chislo < cel:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")