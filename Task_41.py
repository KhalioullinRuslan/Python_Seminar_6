# Задача №41. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5
# 1 2 3 4 5
# Вывод: 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2
# (каждое число вводится с новой строки)

# Решение 1
# from random import randint

# while(True):
#     sp = [randint(0,5) for _ in range(10)]
#     count = 0
#     print(sp)
#     for i in range(1,len(sp)-1):
#         if sp[i-1] < sp[i] and sp[i+1] < sp[i]:
#             count+=1
#     print(count)
#     inp = input()
#     if inp == "q": exit()

# Решение 2
from random import randint


def count_n(sp, j=0):
    for i in range(1, len(sp)-1):
        if sp[i-1] < sp[i] and sp[i] > sp[i+1]:
            j += 1
    print(j)


n = int(input('Введите количество: '))

for i in range(4):
    lst1 = [randint(1, 9) for _ in range(n)]
    print(lst1)
    count_n(lst1)