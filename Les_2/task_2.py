# Для натурального n создато словарь индекс-значеие, состоящий из элементов последовательности 3n+1.
n = int(input("Введите число N "))
d = dict()  # dict создает пустой словарь d = {}
j = 1
for i in range(n):
    d[j] = 3 * j + 1
    j += 1
print(d)
