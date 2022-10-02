# Для натурального n создать список, состоящий из элементов последовательности 3n+1.


def f(b):
    a = []
    for c in range(1, b+1): 
        n = 3 * c + 1
        a.append(n)
    return print(a)
    

N = int(input('Введите значение N ' '\n'))
f(N)

