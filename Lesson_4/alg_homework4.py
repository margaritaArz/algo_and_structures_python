import random
import cProfile

# с рекурсией:

number = random.randint(0, 100)
try_count = 0


def guess_game(number, try_count):
    answer = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
    try_count += 1

    # Base case
    if try_count < 10:
        # Recursive case
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


cProfile.run('guess_game(number, try_count)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   24.795   24.795 <string>:1(<module>)
      6/1    0.000    0.000   24.795   24.795 alg_lesson3.py:7(guess_game)
        6    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        6    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   24.795   24.795 {built-in method builtins.exec}
        6   24.794    4.132   24.794    4.132 {built-in method builtins.input}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Через циклы:

import random
import cProfile

number_1 = random.randint(0, 100)
try_count_1 = 0


def guess_game_1(number_1, try_count_1):
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


cProfile.run('guess_game_1(number_1, try_count_1)')

"""
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   39.209   39.209 <string>:1(<module>)
        1    0.000    0.000   39.209   39.209 alg_lesson3.py:21(guess_game_1)
       11    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       11    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   39.209   39.209 {built-in method builtins.exec}
       11   39.209    3.564   39.209    3.564 {built-in method builtins.input}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Итог: с циклами быстрее: 3.564 против 4.132 в коде с рекурсией.

"""
Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования Решета Эратосфена;
Использовать алгоритм решето Эратосфена
"""

"""
Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования Решета Эратосфена;
Использовать алгоритм решето Эратосфена
"""
# без использования Решета Эратосфена

N = int(input('вывод простых чисел до числа: '))
lst = [] * N

for i in range(N):
    lst.append(i)

lst[1] = 0

prime_number = []
p = 2
for i in range(N):
    if p * p <= lst[i]:
        if lst[i] == 1 or lst[i] % p == 0:
            print(f'Число {lst[i]} не является простым')
            p += 1
    elif lst[i] % 2 != 0 or lst[i] == 2:
        prime_number.append(i)

print(f'Простые числа {prime_number}')

# с использование решета Эратосфена

n = int(input("вывод простых чисел до числа ... "))
a = [0] * n
for i in range(n):
    a[i] = i

a[1] = 0

m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1

b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])

del a
print(b)







