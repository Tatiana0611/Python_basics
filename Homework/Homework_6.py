# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# First version

num_list = [2, 3, 5, 9, 3]
num_sum = 0
print(f'{num_list} -> на нечетных позициях элементы', end = ": ")
for i in range(1, len(num_list), 2):
    print(num_list[i], end = ", ")
    num_sum += num_list[i]
print(f'ответ: {num_sum}')


# Second version

num_list = [2, 3, 5, 9, 3]
print(sum(num_list[1::2]))


# Third version

num_list = [2, 3, 5, 9, 3]
odd_sum = sum([value for i, value in enumerate(num_list) if i%2])
print(odd_sum)

#################################################################################

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# First version

nums = [1, 2, 3, 2, 3, 1, 5, 2, 5, 2, 5]
print(list(set(nums)))


# Second version

nums = [1, 2, 3, 2, 3, 1, 5, 2, 5, 2, 5]
uniq_nams = []
for elem in nums:
    if elem not in uniq_nams:
        uniq_nams.append(elem)
print(uniq_nams)


# Third version

nums = list(map(int, input().split()))
uniq_nams = []
[uniq_nams.append(elem) for elem in nums if elem not in uniq_nams]
print(uniq_nams)


# Fourth version
# generate list of once appearing elements

nums = list(map(int, input().split()))
uniq_nams = list(filter(lambda elem: nums.count(elem) == 1, nums))
print(uniq_nams)

#################################################################################

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# First version

num_list = [1.66, 1.22, 3.33, 5.11, 10.01]
new_list = []
for i in range(len(num_list)):
    new_list.append(round((num_list[i] % 1), 3))
print(num_list)
print(f'max: {max(new_list)}, min: {min(new_list)}')
print(f'ответ: {max(new_list) - min(new_list)}')


# Second version

num_list = [1.66, 1.22, 3.33, 5.11, 10]
new_list = [(num % 1) for num in num_list if isinstance(num, float)]
print(f'max: {round(max(new_list), 2)}, min: {round(min(new_list), 2)}')
print(f'ответ: {round(max(new_list), 2) - round(min(new_list), 2)}')


# Third version

num_list = [1.66, 1.22, 3.33, 5.11, 10]
float_list = list(filter(lambda x: type(x) is float, num_list))
print(float_list)
new_list = list(map(lambda x: round(x % 1, ndigits = 2), float_list))
print(new_list)
print(f'max: {max(new_list)}, min: {min(new_list)}')
print(f'ответ: {max(new_list) - min(new_list)}')

#################################################################################

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# First version

num_list = [2, 3, 4, 5, 6]
new_list = []
for i in range(int(len(num_list) / 2 + len(num_list) % 2)):
    new_list.append(num_list[i] * num_list[len(num_list) - 1 - i])
print(f'{num_list} => {new_list}')


# Second version

num_list = [2, 3, 4, 5, 6]
len = len(num_list) // 2 + len(num_list) % 2

first_list = num_list[:len]
second_list = num_list[:-len-1:-1]

print(first_list)
print(second_list)

for first_list_elem, second_list_elem in zip(first_list, second_list):
	print(first_list_elem * second_list_elem, end = ' ')

#################################################################################

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# First version

number = int(input('Введите число: '))
list_values = [round(((1 + (1 / i)) ** i)) for i in range(1, number + 1)]
dictionary = {}
for i in range(number):
    dictionary[i+1] = list_values[i]
print(dictionary)
print(sum(list_values))


# Second version

new_list = list(map(lambda x: round((1 + (1 / x)) ** x, ndigits=3), [x for x in range(1, int(input('Введите число: '))+1)]))
print(new_list)
print(sum(new_list))