'''''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''''


import random

#вариант 1:
from memory_profiler import profile

@profile
def bubble_sort(bubble_list):
    n = 1
    while n < len(bubble_list):
        for i in range(len(bubble_list)-n):
            if bubble_list[i] > bubble_list[i+1]:
                bubble_list[i],bubble_list[i+1] = bubble_list[i+1], bubble_list[i]
        n += 1
    print(bubble_list)

bubble_list = [random.randint(-100, 100) for _ in range(10)]

bubble_sort(bubble_list)

#вариант 2
from random import randint

N = 10
bubble_list = []

@profile
def bubble_sort(bubble_list, N):
        for i in range(N):
            bubble_list.append(randint(-100, 100))
        print(bubble_list)

        for i in range(N - 1):
            for j in range(N - i - 1):
                if bubble_list[j] > bubble_list[j + 1]:
                    bubble_list[j], bubble_list[j + 1] = bubble_list[j + 1], bubble_list[j]
        print(bubble_list)


bubble_sort(bubble_list, N)

'''''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''''

#lst_random = [random.randint(0, 50) for _ in range(10)]

import timeit
import random

lst_random = [random.randint(0, 50) for _ in range(12)]
print(lst_random)

def merge_sort(lst_random):
    if len(lst_random) > 1:
        center = len(lst_random) // 2
        left = lst_random[:center]
        right = lst_random[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_random[k] = left[i]
                i += 1
            else:
                lst_random[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_random[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_random[k] = right[j]
            j += 1
            k += 1
            return lst_random

merge_sort(lst_random)
print('Отсортированный массив:', lst_random)

print(timeit.timeit("merge_sort(lst_random)", \
    setup="from __main__ import merge_sort, lst_random", number=10))


'''''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
'''''

import random
from random import randint
from statistics import median

m = (random.randint(0, 100))
size = 2 * m + 1
range_ = 30

massive = [randint(0, range_) for i in range(size)]
print(massive)

left = 0
right = len(massive) - 1

def mediana_found(massive):
    print(median(massive))


mediana_found(massive)
