# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = 0.001
print(f'при d = {d}, π = {round((pi // d * d), 10)}')


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = 245
factors = []

while num % 2 == 0:
    factors.append(2)
    num /= 2

for i in range(3, int((num) ** 0.5) + 1, 2):
    while num % i == 0:
        factors.append(i)
        num /= i

if num > 2:
    factors.append(int(num))

print(factors)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

nums = [1, 2, 3, 2, 3, 1, 5, 2, 5, 2, 5]

# Первый вариант
print(list(set(nums)))

# Второй вариант
uniq_nams = []
for elem in nums:
    if elem not in uniq_nams:
        uniq_nams.append(elem)
print(uniq_nams)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 2

coeff_list = [randint(0, 100) for i in range(k + 1)]
print(coeff_list)

df = open('polynom.txt','w')
for i in range(k):
    if coeff_list[i] == 0:
        i -= 1
    elif coeff_list[i] == 1:
        df.write(f'x ^ {k - i} + ')
        i -= 1
    elif i == k - 1:
        df.write(f'{coeff_list[i]} * x + ')
        i -= 1  
    else:
        df.write(f'{coeff_list[i]} * x ^ {k -i} + ')
        i -= 1
df.write(f'{coeff_list[-1]} = 0')
df.close()

# Второй вариант цикла
# df = open('polynom','w')
# i = k
# while i > 0:
#     if coeff_list[len(coeff_list) - 1 - i] == 0:
#         i -= 1
#     elif coeff_list[len(coeff_list) - 1 - i] == 1:
#         df.write(f'x ^ {i} + ')
#         i -= 1
#     else:
#         df.write(f'{coeff_list[len(coeff_list) - 1 - i]} * x ^ {i} + ')
#         i -= 1
# if not coeff_list[len(coeff_list) - 1 - i] == 0:
#     df.write(f'{coeff_list[len(coeff_list) - 1]}')
# df.close()


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('polynom1.txt', 'r') as data:
    polynom1 = data.readline()
    print(polynom1)

with open('polynom2.txt', 'r') as data:
    polynom2 = data.readline()
    print(polynom2)

result_polynom = [str(int(polynom1[0]) + int(polynom2[0]))]
for i in range(1, 12):
    result_polynom.append(polynom1[i])
result_polynom.append(str(int(polynom1[12]) + int(polynom2[12])))
for i in range(13, 20):
    result_polynom.append(polynom1[i])
result_polynom.append(str(int(polynom1[20]) + int(polynom2[20])))
for i in range(21, 25):
    result_polynom.append(polynom1[i])
#print(result_polynom)Lwq

print(''.join(result_polynom))