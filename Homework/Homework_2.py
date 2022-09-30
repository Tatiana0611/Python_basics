# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите число: ')
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(f'Сумма цифр в введенном числе: {sum}')

####################################################################

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# list = []
# multiplication = 1
# for i in range(1, number + 1):
#     multiplication *= i
#     list.append(multiplication)
# print(list)

####################################################################

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# number = int(input('Введите число: '))
# list_values = [round(((1 + (1 / i)) ** i)) for i in range(1, number + 1)]
# dict = {}
# for i in range(number):
#     dict[i+1] = list_values[i]
# print(dict)
# print(sum(list_values))


####################################################################

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
# number = int(input('Введите число: '))
# list = [randint(-number, number) for i in range(number)]
# print(list)
# print(list[1]*list[2])
positions = []
path = 'file.txt'
with open(path) as p:
    for line in p:
        positions.append(line)
print(positions)


####################################################################

# Реализуйте алгоритм перемешивания списка.