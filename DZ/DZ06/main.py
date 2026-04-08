# # 1)
# n = int(input("Введите количество элементов: "))
# a = []
# i = 0
# while i < n:
#     x = int(input("Введите число: "))
#     a.append(x)
#     i += 1
# print("Элементы с чётными индексами:")
# i = 0
# while i < len(a):
#     print(a[i], end=" ")
#     i += 2
# print()
#
# # 2
# n = int(input("Введите количество элементов: "))
#
# a = []
# i = 0
# while i < n:
#     x = int(input("Введите число: "))
#     a.append(x)
#     i += 1
# print("Элементы, большие предыдущего:")
# i = 1
# while i < len(a):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
#     i += 1
# print()

##3
#
# n = int(input("Введите высоту треугольника: "))
#
#
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1
#
# # перевернутыц
# n = int(input("Введите высоту треугольника: "))
#
# i = n
# while i >= 1:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i -= 1   # уменьшаем
#
# size = int(input("Введите размер поля: "))
# symbol = int(input("Кол-во символов: "))
# i = 0
# while i < size:
#     j = 0
#     while j < symbol:
#         n = 0
#         while n < size:
#             m=0
#             while m< symbol:
#                 if (i + n)%2==0:
#                     print("*", end='')
#                 else:
#                     print(" ", end='')
#                 m+=1
#             n += 1
#         print()
#         j += 1
#
#     i += 1
