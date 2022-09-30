# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число: ')
digits_sum = 0
for i in number:
    if i.isdigit():
        digits_sum += int(i)
print(f'Сумма цифр в числе: {digits_sum}')

####################################################################

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
numbers_list = []
multiplication = 1
for i in range(1, number + 1):
    multiplication *= i
    numbers_list.append(multiplication)
print(numbers_list)

####################################################################

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input('Введите число: '))
list_values = [round(((1 + (1 / i)) ** i)) for i in range(1, number + 1)]
dictionary = {}
for i in range(number):
    dictionary[i+1] = list_values[i]
print(dictionary)
print(sum(list_values))


####################################################################

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
number = int(input('Введите число N: '))
numbers_list = [randint(-number, number) for i in range(number)]
print(f'Список из N элементов: {numbers_list}')

with open('file.txt', 'r') as data:
    positions = data.read().splitlines()
data.close()
print(f'Указанные позиции: {positions}')

multiplication = numbers_list[int(positions[0])] * numbers_list[int(positions[1])]
print(f'Произведение элементов списка на указанных позициях: {multiplication}')

####################################################################

# Реализуйте алгоритм перемешивания списка.

import random
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(new_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    new_list[i], new_list[j] = new_list[j], new_list[i]
print (new_list)