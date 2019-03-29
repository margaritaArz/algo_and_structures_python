'''''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''''

#версия Python: 3.7, разрядность 32

from random import random
import sys
import timeit
from memory_profiler import profile

@profile
def testFunc():
    N = 10
    a = []
    for i in range(N):
        a.append(int(random() * 100))
        print("%3d" % a[i], end='')
    print()

    if a[0] > a[1]:
        min1 = 0
        min2 = 1
    else:
        min1 = 1
        min2 = 0

    for i in range(2, N):
        if a[i] < a[min1]:
            b = min1
            min1 = i
            if a[b] < a[min2]:
                min2 = b
        elif a[i] < a[min2]:
            min2 = i

    print("№%3d:%3d" % (min1 + 1, a[min1]))
    print("№%3d:%3d" % (min2 + 1, a[min2]))
    print(sys.getrefcount(min1)) #149 ссылок на 'min1'. Видимо название переменной часто встречается во внутриних файлах.
    
    del min1

testFunc()

'''''
Line #    Mem usage    Increment   Line Contents
================================================
    15     11.5 MiB     11.5 MiB   @profile
    16                             def testFunc():
    17     11.5 MiB      0.0 MiB       N = 10
    18     11.5 MiB      0.0 MiB       a = []
    19     11.5 MiB      0.0 MiB       for i in range(N):
    20     11.5 MiB      0.0 MiB           a.append(int(random() * 100))
    21     11.5 MiB      0.0 MiB           print("%3d" % a[i], end='')
    22     11.5 MiB      0.0 MiB       print()
    23
    24     11.5 MiB      0.0 MiB       if a[0] > a[1]:
    25                                     min1 = 0
    26                                     min2 = 1
    27                                 else:
    28     11.5 MiB      0.0 MiB           min1 = 1
    29     11.5 MiB      0.0 MiB           min2 = 0
    30
    31     11.5 MiB      0.0 MiB       for i in range(2, N):
    32     11.5 MiB      0.0 MiB           if a[i] < a[min1]:
    33     11.5 MiB      0.0 MiB               b = min1
    34     11.5 MiB      0.0 MiB               min1 = i
    35     11.5 MiB      0.0 MiB               if a[b] < a[min2]:
    36     11.5 MiB      0.0 MiB                   min2 = b
    37     11.5 MiB      0.0 MiB           elif a[i] < a[min2]:
    38     11.5 MiB      0.0 MiB               min2 = i
    39
    40     11.5 MiB      0.0 MiB       print("№%3d:%3d" % (min1 + 1, a[min1]))
    41     11.5 MiB      0.0 MiB       print("№%3d:%3d" % (min2 + 1, a[min2]))
    42     11.5 MiB      0.0 MiB       print(sys.getrefcount(min1))
    43     11.6 MiB      0.0 MiB       del min1
'''''
#с рекурсией:
import random

number = random.randint(0, 100)
try_count = 0

@profile
def guess_game(number, try_count):
    answer = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
    try_count += 1

    if try_count < 10:
        if answer > number:
            print('Вы ввели слишком большое число!', 'Число попыток:', try_count)
            guess_game(number, try_count)

        elif answer < number:

            print('Вы ввели слишком маленькое число!', 'Число попыток:', try_count)
            guess_game(number, try_count)

        if answer == number:
            print('Поздравляю вы выиграли!', number)

        if try_count >= 10:
            print('Вы проиграли. Загаданое число:', number)
print(sys.getrefcount(guess_game)) #2 ссылки потому что название более специфичное и реже встречается.
guess_game(number, try_count)

'''''
Line #    Mem usage    Increment   Line Contents
================================================
    84     11.6 MiB     11.6 MiB   @profile
    85                             def guess_game(number, try_count):
    86     11.6 MiB      0.0 MiB       answer = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
    87     11.6 MiB      0.0 MiB       try_count += 1
    88
    89     11.6 MiB      0.0 MiB       if try_count < 10:
    90     11.6 MiB      0.0 MiB           if answer > number:
    91                                         print('Вы ввели слишком большое число!', 'Число попыток:', try_count)
    92                                         guess_game(number, try_count)
    93
    94     11.6 MiB      0.0 MiB           elif answer < number:
    95
    96                                         print('Вы ввели слишком маленькое число!', 'Число попыток:', try_count)
    97                                         guess_game(number, try_count)
    98
    99     11.6 MiB      0.0 MiB           if answer == number:
   100     11.6 MiB      0.0 MiB               print('Поздравляю вы выиграли!', number)
   101
   102     11.6 MiB      0.0 MiB           if try_count >= 10:
   103                                         print('Вы проиграли. Загаданое число:', number)
'''''

#Через циклы:

import random

@profile

def guess_game_1():
    number_1 = random.randint(0, 100)
    try_count_1 = 0
    answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))

    while try_count_1 < 10:
        if answer_1 > number_1:
            try_count_1 += 1
            print(f'Вы ввели слишком большое число! Число попыток: {try_count_1}')
            answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))

        elif answer_1 < number_1:
            try_count_1 += 1
            print('Вы ввели слишком маленькое число!', f'Число попыток: {try_count_1}')
            answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))

        if answer_1 == number_1:
            print('Поздравляю вы выиграли!', number_1)
            break

        if try_count_1 >= 10:
            print('Вы проиграли. Загаданое число:', number_1)
            break
guess_game_1()

'''''
Line #    Mem usage    Increment   Line Contents
================================================
   136     11.6 MiB     11.6 MiB   @profile
   137
   138                             def guess_game_1():
   139     11.6 MiB      0.0 MiB       number_1 = random.randint(0, 100)
   140     11.6 MiB      0.0 MiB       try_count_1 = 0
   141     11.6 MiB      0.0 MiB       answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
   142
   143     11.6 MiB      0.0 MiB       while try_count_1 < 10:
   144     11.6 MiB      0.0 MiB           if answer_1 > number_1:
   145     11.6 MiB      0.0 MiB               try_count_1 += 1
   146     11.6 MiB      0.0 MiB               print(f'Вы ввели слишком большое число! Число попыток: {try_count_1}')
   147     11.6 MiB      0.0 MiB               answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
   148
   149     11.6 MiB      0.0 MiB           elif answer_1 < number_1:
   150     11.6 MiB      0.0 MiB               try_count_1 += 1
   151     11.6 MiB      0.0 MiB               print('Вы ввели слишком маленькое число!', f'Число попыток: {try_count_1}')
   152     11.6 MiB      0.0 MiB               answer_1 = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
   153
   154     11.6 MiB      0.0 MiB           if answer_1 == number_1:
   155     11.6 MiB      0.0 MiB               print('Поздравляю вы выиграли!', number_1)
   156     11.6 MiB      0.0 MiB               break
   157
   158     11.6 MiB      0.0 MiB           if try_count_1 >= 10:
   159                                         print('Вы проиграли. Загаданое число:', number_1)
   160                                         break
'''''

#По результатам вышло, что с рекурсией и циклами одинакоое количество памяти код занимает.
