# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# from time import time
# print(int(time() % 1 * 100))
# print(time())


# Определить, присутствует ли в заданном списке строк, некоторое число

# new_list = ['1', '23', '5', '3']
# number = 3
# nul = 0
# for elem in new_list:
#     if str(number) in elem:
#         print('yes')
#         print(new_list.index(elem, nul)) # ищет позицию элемента i начиная с nul
#         nul = new_list.index(elem, nul) + 1

# new_list = ['1', '23', '5', '3']
# number = 3
# for i, elem in enumerate(new_list): # enumerate примерно тоже, что и range, но перебирает и элементы и их индексы
#     if str(number) in elem:
#         print('yes')
#         print(i)


# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

new_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "ячс", "цук"]
find_str = "йцукен"
n = 0
for i in range(len(new_list)):
    if new_list[i] == find_str:
        n += 1
        if n == 2:
            print(i)
            break
else:
    print(-1) 
 