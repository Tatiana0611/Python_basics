# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

# num_str = '1 3 4 6 7 8'
# num_list = [int(i) for i in num_str.split()]
# print(f'max: {max(num_list)}, min: {min(num_list)}')

# num_str = '1 3 4 6 7 8'
# num_list = list(map(int, num_str.split()))
# print(f'max: {max(num_list)}, min: {min(num_list)}')


# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

# a, b, c = 8, 4, 2
# disc = b ** 2 - 4 * a * c
# if disc > 0:
#     x_1 = (- b + disc ** 0.5) / (2 * a)
#     x_2 = (- b - disc ** 0.5) / (2 * a)
#     print(f' x1 = {x_1}, x2 = {x_2}')
# elif disc == 0:
#     x = - b / (2 * a)
#     print(x)
# else:
#     print('Нет корней')


# Найти НОК двух чисел

# a, b = 4, 6
# nok = max(a, b)
# while not (nok % a == 0 and nok % b == 0):
#     nok += max(a, b)
# print(nok)
