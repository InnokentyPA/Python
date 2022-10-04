# 2 Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
# list_1 = [3, 6, 5, 10, 12]
# max_num = list_1[0]
# for i in list_1:
#     if i > max_num:
#         max_num = i
# print(max_num)

entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введите список: ", entered_list)
num_list = list(map(int, entered_list))
print("Максимальное число в списке: ", max(num_list))