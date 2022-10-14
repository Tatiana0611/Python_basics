# LAMBDA

# def f(x):
#     return x ** 2
# print(type(f), f(3))

# g = f # в переменную g кладем переменную f
# print(type(g), g(3))

# def calc1(x):
#     return x + 10
# print(calc1(10))

# def calc2(x):
#     return x * 10
# print(calc2(10))

# def math(oper, x):
#     print(oper(x))
# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):  # sum = lambda x, y: x + y
#     return x + y
# f = sum
# sum = lambda x, y: x + y + 1

# def mult(x, y):
#     return x * y

# def calc(oper, a, b):
#     print(oper(a, b))
#     # return oper(a, b)

# calc(mult, 4, 5)
# calc(sum, 4, 5)
# calc(lambda x, y: x + y + 1, 4, 5)




# LIST COMPREHENSION

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditionaal> item in iterable (if conditional)]

# list = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(1, 101) if i % 2 == 0]
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0] # список кортежей
# print(list)

# def f(x):
#     return x ** 3
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # список кортежей
# print(list)

# path = 'lec_3.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)



# MAP

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, input().split())
# for e in data:
#     print(e)

# data = list(map(int, '1 2 3 4 6 4'.split())) # без list второй цикл for не сработает
# for e in data:
#     print(e)
# print('--')
# for e in data:
#     print(e * 10)

def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 38'.split()
res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)




# FILTER

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# data = '1 2 3 5 8 15 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)




# ZIP

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 322, 444]
data  = list(zip(users, ids))
print(data)
# data  = list(zip(users, ids, salary))
# print(data)



# ENUMERATE

# print(list(enumerate(['Казань'], ['Смоленск'], ['Рыбки'], ['Чикаго'])))
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data  = list(enumerate(users))
# print(data)





















