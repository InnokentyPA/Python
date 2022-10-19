# Напишите программу, которая определит позицию второго вхождения строки в списке либо
# сообщит, что её нет.
ent_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", ent_list)
print("Введите число для поиска: ")
n = input()
print(ent_list.count(n))
count = 0
if ent_list.count(n) >= 2:
    for i in range(len(ent_list)):
        if ent_list[i] == n:
            count += 1
            if count == 2:
                print(f"Индекс второй позиции {i}")
else:
    print("Второй позиции нет.")