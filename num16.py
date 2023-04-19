# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

import main

# def num1618():
#     N = int(input("Введите размер массива "))
#     array_AN = []
#     i = 1
#     for i in range(N):
#         a = int(input("Введите число для массива "))
#         array_AN.append(a)
#         i += 1
#
#     number_X = int(input("Введите число X "))
#     return N,array_AN,number_X


N,array_AN,number_X=main.num1618()

count = 0

for el in array_AN:
    if el == number_X:
        count+=1
print(count)
