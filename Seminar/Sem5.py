# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# num_str = '1 2 3 4 5 6 8 9'
# num_list = list(map(int, num_str.split()))

# for i in range(1, len(num_list)):
#     if not (num_list[i] - 1) == num_list[i - 1]:
#         print(num_list[i] - 1)


# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

num_list = [1, 5, 2, 3, 4, 6, 1, 7]

new_list = [num_list[0]]
max = num_list[0]
for i in range(1, len(num_list) - 1):
    if num_list[i] > max:
        new_list.append(num_list[i])
        max = num_list[i]
print(new_list)