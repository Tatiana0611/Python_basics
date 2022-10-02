# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# from random import randint
# n = int(input('Введите число: '))
# list = [randint(-100, 100) for i in range(n)]
# print(list)


# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input('Введите число: '))
# result = dict()
# for i in range(1, n + 1):
#     result[i] = 3 * i + 1
# print(result)

# list = []
# for i in range(1, n + 1):
#     element = [i, 3 * i + 1]
#     list.append(element)
# print(dict(list))

# print({item: 3*item+1 for item in range(1, 6+1)})

#Напишите программу, в которой пользователь будет задавать две строки, а программа определять количество вхождений одной строки в другой
# str_1 = input('Введите строку 1: ')
# str_2 = input('Введите строку 2: ')
# print(str_1.count(str_2))

# count = 0
# for i in str_1:
#     if i == str_2:
#         count += 1
# print(count)

