# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input("Введите число N "))
d = {} 
j = 1
answer = 0
for i in range(n):
    d[j] = 3 * j + 1
    answer +=d[j]
    j += 1
print(d)
print(answer)