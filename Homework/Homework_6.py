# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# First version

# num_list = [2, 3, 5, 9, 3]
# num_sum = 0
# print(f'{num_list} -> на нечетных позициях элементы', end = ": ")
# for i in range(1, len(num_list), 2):
#     print(num_list[i], end = ", ")
#     num_sum += num_list[i]
# print(f'ответ: {num_sum}')


# Second version

# num_list = [2, 3, 5, 9, 3]
# print(sum(num_list[1::2]))


# Third version

# num_list = [2, 3, 5, 9, 3]
# odd_sum = sum([value for i, value in enumerate(num_list) if i%2])
# print(odd_sum)

##########################################################################

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# nums = [1, 2, 3, 2, 3, 1, 5, 2, 5, 2, 5]

# First version

# print(list(set(nums)))


# Second version

# uniq_nams = []
# for elem in nums:
#     if elem not in uniq_nams:
#         uniq_nams.append(elem)
# print(uniq_nams)


# Third version

# nums = list(map(int, input().split()))
# uniq_nams = []
# [uniq_nams.append(elem) for elem in nums if elem not in uniq_nams]
# print(uniq_nams)


# Fourth version
# list of once appearing elements

# nums = list(map(int, input().split()))
# uniq_nams = list(filter(lambda elem: nums.count(elem) == 1, nums))
# print(uniq_nams)

###########################################################################

