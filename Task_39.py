# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод: 3 3 2 12
# (каждое число вводится с новой строки)

# Решение 1
# from random import randint

# n = int(input("Введите количество элементов в первом массиве: "))
# m = int(input("Введите количество элементов во втором массиве: "))

# sp1 = [randint(1,10) for _ in range(n)]
# sp2 = [randint(1,10) for _ in range(m)]
# sp3 = []

# print(sp1)
# print(sp2)

# for elem in sp1:
#     if elem not in sp2:
#         sp3.append(elem)

# print(sp3)


# Решение 2
from random import randint


def compare(sp1, sp2):
    sp = []
    for i in sp1:
        if i not in sp2:
            sp.append(i)
    print(sp)


try:
    while True:
        n = int(input('Введите количество 1: '))
        lst1 = [randint(1, 9) for _ in range(n)]
        print(lst1)
        m = int(input('Введите количество 2: '))
        lst2 = [randint(1, 9) for _ in range(m)]
        print(lst2)
        compare(lst1, lst2)
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()