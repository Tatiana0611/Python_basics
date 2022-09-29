# FILES
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# write in file
# colors = ['red', 'green', 'blue'] # файловая переменная
# data = open('file.txt', 'a') # если файла нет, то он создастся. 'а' дописывает данные
# # data = open('file.txt', 'w') # 'w' перезаписывает данные
# data.writelines(colors)
# data.writelines('\nline')
# data.write('\nline1')
# data.close() # необходимо разорвать связь файла с файловой переменной

# write in file
# with open('file1.txt', 'w') as data:
#     data.write('line1')
#     data.write('line2')
# data.close()

# #read from file
# path = 'file1.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


#FUNCTION

# import hello as h
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!')) #count не указывается т.к. ему уже присвоено значение
# print(new_string(4))
# print(new_string('4'))

# def concatenation(*params):
#     res: str = "" # : присваивается тип для res - str, исходное значение - пустая строка
#     # res: int = 0 # так можно, но лучше не использовать
#     # res = "" # ил res = 0 Можно не указывать тип 
#     for item in params:
#         res += item
#     return res
# print(concatenation('1', '2', '3', '4')) # 1234 если res: str = ""
# # print(concatenation(1, 2, 3, 4)) # 1234 если res: int = 0


#РУКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) #[1, 1, 2, 3, 5, 8, 13, 21, 34]


# TUPLES (Неизменяемые списки)

# a = (3, 4, 5, 7)
# b = (3,) # кортеж из одного элемента
# print(a) # (3, 4, 5, 7)
# print(a[0]) # 3
# print(a[-1]) # 7
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue']) # преобразование списка в кортеж
# print(t[0]) # red
# print(t[2]) # blue
# print(t[-2]) # green
# for _ in t:
#     print(_)
# # t[0] = 'red' # error

# red, green, blue = t # распаковка кортежа в отдельные переменные
# print('r: {} g: {} b: {}'.format(red, green, blue)) # r: red g: green b: blue


#DICTIONARY (неупорядоченные коллекции произвольных объектов с доступом по ключу)

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left']) # ←
# for k in dictionary.keys():
#     print(k) # up left down right
# for k in dictionary.values():
#     print(k) # ↑ ← ↓ →
# for k in dictionary:
#     print(k)
# for v in dictionary:
#     print(dictionary[v])
# print(dictionary)
# dictionary['left'] = 'up'
# print(dictionary['left'])
# del dictionary['left']
# print(dictionary)
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

#SET (МНОЖЕСТВА)

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors) # {'red', 'blue', 'green'}
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.remove('red') #вызовет ошибку, если элемента нет
# print(colors)
# colors.discard('red') #вызовет ошибку, если элемента нет
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b)
# print(u) #{1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)
# print(i) # {8, 2, 5}
# dl = a.difference(b)
# print(dl) # {1, 3}
# dr = b.difference(a)
# print(dr) # {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q) # {1, 21, 3, 13}
# s = frozenset(a) # неизменяемое множество
 

#LISTS
#1. Копируем СПИСОК1 в СПИСОК2, изменяем СПИСОК1, СПИСОК2 тоже меняется. Меняем СПИСОК2, СПИСОК1 тоже меняется
list1 = [1, 2, 3, 4]
# list2 = list1
# for e in list1:
#     print(e)
# for e in list2:
#     print(e)
# list1[1] = 13
# for e in list1:
#     print(e)
# for e in list2:
#     print(e)
# list2[1] = 113
# for e in list1:
#     print(e)
# for e in list2:
#     print(e)
# print(list1.pop(2)) # удаление 3го элемента
# print(list1.pop()) # удаление последнего элемента
# print(list1)
# list1.insert(2, 11) # на 2 позицию ставится элемент 11
# print(list1)
# list1.append(11) # в конец ставится элемент 11
# print(list1)











