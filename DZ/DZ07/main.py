
a = [3, 7, 2, 5, 2, 8, 3, 9, 5, 1, 7, 4, 3, 6, 1]
print("Исходнный список:", a)

udalit = [8, 9, 4, 6]
print("Удалить значения:", udalit)

noviy = []
i = 0
while i < len(a):
    if a[i] not in udalit:
        noviy.append(a[i])
    i += 1

print("После удаления:", noviy)

n = len(noviy)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if noviy[j] > noviy[j + 1]:
            temp = noviy[j]
            noviy[j] = noviy[j + 1]
            noviy[j + 1] = temp
        j += 1
    i += 1

print("Отсортированный список:", noviy)