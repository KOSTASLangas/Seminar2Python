# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.


def f(n):
    for i in range(n): 
        N = (-3) ** i
        print(N, end= '  ')
    return


N = int(input('Введите значение N ' '\n'))
f(N)