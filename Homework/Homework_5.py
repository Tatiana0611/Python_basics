# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
 
with open('HW5_1.txt', 'r') as f:
    text = f.read().split()

print(text)

res = list(filter(lambda x: not 'abc' in x, text))

print(res)



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

total_sweets = 2021

player_1 = input('Имя первого игрока: ')
player_2 = input('Имя второго игрока: ')
players = [player_1, player_2]

count = randint(0, 1)
print(f'Первый ход у игрока {players[count % 2]}')

# Когда остается 28 конфет игрок, чей ход является следующим, забирает их все и выигрывает.
while total_sweets > 28:
    take_sweets = int(input(f'\n{players[count % 2]}, возьмите не более 28 конфет. Введите количество конфет: '))
    total_sweets -= take_sweets
    print(f'Количество оставшихся конфет: {total_sweets}')
    count += 1
else:
    print(f'\n{players[count % 2]} берет оставшиеся конфеты в количестве {total_sweets} штук и побеждает!')

# Чтобы забрать все конфеты первый игрок должен всегда брать конфеты в количестве 
# (общее кол-во конфет % (максимальное кол-во конфет за 1 ход + 1)) штук



# Создайте программу для игры в ""Крестики-нолики"".

def draw_fields(field_number):
    print('-------------')
    for i in range(3):
        print(f'| {field_number[i*3]} | {field_number[1 + i*3]} | {field_number[2 + i*3]} |')
        print('-------------')

def check_result(field_number):
    win_number = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_number:
        if field_number[i[0]] == field_number[i[1]] == field_number[i[2]]:
            return field_number[i[0]]
    return False

field_number = list(range(1, 10))
count = 0
win = False

while not win:
    draw_fields(field_number)
    if count % 2 == 0:
        chosen_field = int(input('\nУкажите номер свободного поля, где поставить X: '))
        if (str(field_number[chosen_field - 1]) not in "X0"):
            field_number[chosen_field - 1] = 'X'
    else:
        chosen_field = int(input('\nУкажите номер свободного поля, где поставить 0: '))
        if (str(field_number[chosen_field - 1]) not in 'X0'):
            field_number[chosen_field - 1] = '0'     
    count += 1
    if count > 4:
        temp = check_result(field_number)
        if temp:
            print(f'\nВыиграл, {temp}')
            win = True
            break
    if count == 9:
        print('\nНичья')
        break
draw_fields(field_number)
    


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Сжатие

with open('HW5_input_data.txt', 'r') as data:
    input_data = data.read()

print(input_data)

i = 0
encoded_data = ''

while i <= len(input_data) - 1:
    char = input_data[i]
    count = 1
    j = i
    while j < len(input_data) - 1:
        if input_data[j] == input_data[j + 1]:
            count += 1
            j += 1
        else: 
            break
    encoded_data += str(count) + char
    i = j + 1

print(encoded_data)

with open('HW5_encoded_data.txt', 'w') as data:
    data.write(encoded_data)


# Восстановление

with open('HW5_encoded_data.txt', 'r') as data:
    encoded_data = data.read()

print(encoded_data)

decoded_data = ''
count = ''
for char in encoded_data:
    if char.isdigit():
        count += char
    else:
        decoded_data += char * int(count)
        count = ''
        
print(decoded_data)

