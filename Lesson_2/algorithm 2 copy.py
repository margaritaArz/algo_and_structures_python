
"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

print("При вводе 0 в качестве знака операции, программа завершится")

while True:
    operation = (input('Введите знак операции 0, +, -, *, / '))
    if operation == '0':
        break
    if operation in ('*', '+', '-', '/'):
        num1 = int(input("Введите первое число "))
        num2 = int(input("Введите второе число "))
        if operation == '+':
            print(f'{num1} + {num2} = ', num1 + num2)
        if operation == '/':
            if num2 != 0:
                print(f'{num1} / {num2} =', num1 / num2)
            else:
                print("На 0 делить нельзя")
        elif operation == '*':
            print(f'{num1} * {num2} =', num1 * num2)
        if operation == '-':
            print(f'{num1} - {num2} =', num1 - num2)
    else:
        operation = (input('Введите правильный знак операции. Введите знак операции 0, +, -, *, / '))

"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

x = int(input('Введите натуральное число '))
even, odd = 0, 0

while x > 0:
    if x % 2 == 0:
        print(x, 'четное число')
        even +=1
    else:
        print(x, 'нечетное число')
        odd += 1
    x = x // 10
print('нечетных чисел =', odd, 'четных чисел =', even)


#Вариант 2

def recursion():
    n = int(input('Введите натуральное число'))
    n = n // 10
    odd_num = 0
    even_num = 0

    if n > 0:
        if n % 2 == 0:
            print(n, 'четное число')
            even_num += 1
        recursion()
        if n % 2 != 0:
            print(n, 'нечетное число' )
            odd_num += 1
recursion()

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
b = int(input('Введите число = '))
c = 0

def reverse(b, c):

    if b > 0:
        c = c * 10 + b % 10
        b = b // 10
print(b)

reverse(b, c)

#вариант 2

a = int(input('Введите число '))
rest = 0

while a > 0:
    rest = rest * 10 + a % 10
    a = a // 10
print(rest)


"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

a = int(input('Введите количество элементов n '))
def rec(a):
    element = 1
    sum = 0
    if sum < a:
        sum += element
        element /= -2
    rec(a)
    print(sum)
rec(a)

"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random

number = random.randint(0, 100)

def guess_game():
    answer = int(input('Загадано число от 0 до 99. Угадай загаданное число '))
    try_count = 0

    # Base case
    if try_count < 10:
    # Recursive case
        if answer > number:
            print('Вы ввели слишком большое число')
            guess_game()
            try_count =+1

        elif answer < number:
            print('Вы ввели слишком маленькое число')
            guess_game()
            try_count =+ 1

        if answer == number:
            print('Поздравляю вы выиграли!', number)

        elif try_count == 10:
            print('Вы проиграли. Загаданое число:', number)

guess_game()


"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = int(input())
print(factorial(n))

"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


