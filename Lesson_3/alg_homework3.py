# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

massive = [0]*8

for i in range(2, 100):
    for j in range(2, 10):
        if i%j == 0:
            massive[j - 2] += 1
i = 0
while i < len(massive):
    print(i + 2, ' - ', massive[i])
    i += 1

"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

massive_1 = [8, 3, 15, 6, 4, 2]

massive_2 = []

for i in range(6):
    if massive_1[i] % 2 == 0:
          massive_2.append(i)
print(massive_1)
print('Позиция четных чисел', massive_2)

#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import random

N = 6
count_list = [0]*N

for i in range(N):
    count_list[i] = int(random()*100)
print(count_list[i], end= ' ')
min = 0
max = 0
for i in range(N):
    if count_list[i] > count_list[max]:
        max = i
    elif count_list[i] < count_list[min]:
        min = i
count_list[max], count_list[min] = count_list[min], count_list[max]

print(count_list)
print(count_list[max], count_list[min])

# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random

N = 17
new_list = [0] * N

for i in range(N):
    new_list.append(int(random()*100))
print(new_list)

max_repeated = 1
num_repeated = new_list[0]

for i in range(N-1):
    repeat = 1
    for k in range(i+1, N):
        if new_list[i] == new_list[k]:
            repeat += 1
        if repeat > max_repeated:
            max_repeated = repeat
            num_repeated = new_list[i]
if max_repeated > 1:
    print(f'Число {num_repeated} встречается {max_repeated} раз(а).')
else:
    print('В массиве нет повторений')

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

arr = [-1, 23, -56, 65, 34, 87, -100]
max_negative = -1
i = 0

while i < len(arr):
    if arr[i] < 0 and arr[max_negative] == -1:
        max_negative = i
    if arr[i] < 0 and arr[i] > arr[max_negative]:
        max_negative = i
    i += 1

print(f'Максимальный отрицательный элемент {[i]}, его индекс {max_negative}')

"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random

N = 7
arr_2 = []*N

for i in range(N):
    arr_2.append(int(random()*100))
print(arr_2)

min = 0
max = 0

for i in range(1, N):
    if arr_2[i] > arr_2[max]:
        max = i
    elif arr_2[i] < arr_2[min]:
        min = i
    if min > max:
        arr_2[max], arr_2[min] = arr_2[min], arr_2[max]

sum = 0
for i in range (arr_2[min]+1, arr_2[max]):
    sum += arr_2[i]

print(sum)

"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

N = 7
arr_3 = []*N

for i in range(N):
    arr_3.append(int(random()*100))
print(arr_3)

min_1 = 0
min_2 = 0

for i in range(1, N):
    if arr_3[i] > arr_3[min_1]:
        min_1 = i
    if arr_3[i] == arr_3[min_1]:
        min_2 = i
print(min_1, min_2)

