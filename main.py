def num1618():
    N = int(input("Введите размер массива "))
    array_AN = []
    i = 1
    for i in range(N):
        a = int(input("Введите число для массива "))
        array_AN.append(a)
        i += 1

    number_X = int(input("Введите число X "))
    return N,array_AN,number_X
