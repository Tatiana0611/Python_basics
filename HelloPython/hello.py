# print('hello, world')

# a = 123
# b = 1.23
# value = None #если необходимо объявить сейчас, а использовать потом
# print(a)
# print(b)
# print(type(value))
# value = 1234
# print(type(value))
# s = 'hello, world'
# ss = "hello, 'world" # или использовать исключение 'hello, \'world'
# sss = 'hello "world'
# print('первая строка', s,'вторая строка', ss,'третья строка', sss)
# print(f'первая строка {s} вторая строка {ss} третья строка {sss}')
# print('первая строка {} вторая строка {} третья строка {}'.format(s, ss, sss))
# print('первая строка {2} вторая строка {1} третья строка {0}'.format(s, ss, sss))
# f = True
# print(f)

# list = [1, 'dd', 2.4]
# print(list)

# print('Enter a')
# a = int(input())
# print('Enter b')
# b = int(input())
# print(a,'+', b, '=', a+b)

# a = 27.46
# b = 3
# c = round(a * b, 5)
# d = a // b
# e = a % b
# f = round(a ** b)
# a += 5
# print(c, d, e, f, a)

# a = 1 < 4 and 5 > 2
# b = 1 == 2
# c = 1 != 2
# aa = 'qwt'
# bb = 'qwt'
# d = aa == bb
# cc = [1, 2, 3]
# dd = [1, 2, 3]
# e = cc == dd
# f = 1 < 2 < 3 < 6
# print(a, b, c, d, e, f)

# g = 2
# k = 6
# l = 9
# print(g < l > k)

# f = 1 > 2 or 4 < 6
# print(f)
# a = [1, 2, 3, 4]
# print(not 2 in a)
# is_odd = not a[0] % 2 #is_odd = a[0] % 2 == 0
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Your name: ')
# if username == 'Masha':
#     print('It is Masha')
# elif username == 'Marina':
#     print('Hello, Marina')
# elif username == 'Ilnar':
#     print('Ilnar - top')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i ** 2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i ** 2)

# list = range(5)
# for i in list:
#     print(i)
# for i in range(5):
#     print(i)
# for i in range(2, 5):
#     print(i)
# for i in range(2, 15, 3):
#     print(i)
# for i in 'qwerty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'
# print(len(text))
# print('еще'in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))
# for c in text:
#     print(c)

# text = 'съешь еще этих мягких французских булок'
# print(text[0])
# print(text[1])
# #print(text[len(text)])
# print(text[len(text)-1])
# print(text[-2])
# print(text[:])
# print(text[:2])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# numbers = list(ran)
# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)
# for e in colors:
#     print(e*2)

# colors.append('grey')
# print(colors == ['red', 'green', 'blue', 'grey'])
# colors.remove('red') # del colors[0]
# print(colors)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2
# print(f(arg))
# print(type(f(arg)))