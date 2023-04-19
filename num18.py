
# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
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


j=0
difference = []
for j in range(N):
    if (array_AN[j] == number_X):
        print(array_AN[j])
        exit(0)
    else:
        if (array_AN[j]>number_X):
            difference.append(array_AN[j]-number_X)
        else:
            difference.append(number_X+array_AN[j])

min_i=0
i=1
for i in range(N):
    if difference[min_i]>difference[i]:
        min_i=i
    elif difference[min_i]==difference[i]:
        if(array_AN[i]>array_AN[min_i]):
            min_i=i

print(array_AN[min_i])