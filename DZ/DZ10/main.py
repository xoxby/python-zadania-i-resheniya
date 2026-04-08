print("Выберите фигуру для расчёта площади:")
print("1 - круг")
print("2 - треугольник")
print("3 - прямоугольник")
print("0 - выход")

while True:
    try:
        vibor = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка! Введите число от 0 до 3.")
        continue

    if vibor == 0:
        print("Выход из программы.")
        break

    if vibor == 1:
        try:
            r = float(input("Введите радиус: "))
            if r < 0:
                print("Радиус не может быть отрицательным.")
                continue
            ploshad = 3.14 * r * r
            print("Площадь круга:", ploshad)
        except ValueError:
            print("Ошибка! Введите число.")

    elif vibor == 2:
        try:
            osnovanie = float(input("Введите основание: "))
            visota = float(input("Введите высоту: "))
            if osnovanie < 0 or visota < 0:
                print("Стороны не могут быть отрицательными.")
                continue
            ploshad = (osnovanie * visota) / 2
            print("Площадь треугольника:", ploshad)
        except ValueError:
            print("Ошибка! Введите число.")

    elif vibor == 3:
        try:
            dlina = float(input("Введите длину: "))
            shirina = float(input("Введите ширину: "))
            if dlina < 0 or shirina < 0:
                print("Стороны не могут быть отрицательными.")
                continue
            ploshad = dlina * shirina
            print("Площадь прямоугольника:", ploshad)
        except ValueError:
            print("Ошибка! Введите число.")

    else:
        print("Неверный выбор. Введите 0, 1, 2 или 3.")