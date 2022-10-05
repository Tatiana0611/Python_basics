# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# num_list = [2, 3, 5, 9, 3]
# num_sum = 0
# print(f'{num_list} -> на нечетных позициях элементы', end = ": ")
# for i in range(1, len(num_list), 2):
#     print(num_list[i], end = ", ")
#     num_sum += num_list[i]
# print(f'ответ: {num_sum}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# num_list = [2, 3, 4, 5, 6]
# new_list = []
# for i in range(int(len(num_list) / 2 + len(num_list) % 2)):
#     new_list.append(num_list[i] * num_list[len(num_list) - 1 - i])
# print(f'{num_list} => {new_list}')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# num_list = [1.66, 1.22, 3.33, 5.11, 10.01]
# new_list = []
# for i in range(len(num_list)):
#     new_list.append(round((num_list[i] % 1), 3))
# print(num_list)
# print(f'max: {max(new_list)}, min: {min(new_list)}')
# print(f'ответ: {max(new_list) - min(new_list)}')

# num_list = [1.66, 1.22, 3.33, 5.11, 10]
# new_list = [(num % 1) for num in num_list if isinstance(num, float)]
# print(f'max: {max(new_list)}, min: {min(new_list)}')
# print(f'ответ: {max(new_list) - min(new_list)}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# dec = 2
# bin = ''
# print(dec, end = " -> ")
# while dec != 0:
#     bin = bin + str(dec % 2)
#     dec //= 2
# print(bin[::-1])

# dec = 2
# print(format(dec, '#b'), format(dec, 'b'))
# print(f'{dec:#b}', f'{dec:b}')


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# k = 8

# fib_list = []

# fib1 = fib2 = 1
# for i in range(k):
#     fib_list.append(fib1)
#     fib1, fib2 = fib2, fib1 + fib2

# fib1, fib2 = 0, 1
# for i in range(k + 1):
#     fib_list.insert(0, fib1)
#     fib1, fib2 = fib2, fib1 - fib2

# print(fib_list)