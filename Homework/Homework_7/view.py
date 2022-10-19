
# show menu
def show_menu():
    print("\nСписок возможных действий:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input('\nВыберите необходимое действие: '))
    print()
    return choice

# show all phone book
# "1. Отобразить весь справочник\n"
def show_phone_book(data):
    for dict in data:
        print(' '.join(f'{k}' for k in dict.values()))

# enter search value (last name or phone number)
def find_value(title):    
    find_value = input(f'{title}: ')
    return find_value 

# find person by last name or phone number
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
def find_person(data, find_key, find_value):
    for dict in data:
        if dict[find_key] == find_value:
            find_person = ' '.join(f'{k}' for k in dict.values())
            print(f'\n{find_person}')
    if not any(dict for dict in data if dict[find_key] == find_value):
        print('\nТакого человека нет в справочнике')

# add person to phone book
# "4. Добавить абонента в справочник\n"
def add_person(data):
    last_name, name, phone, descr = input('Для добавления абонента введите его фамилию, имя, номер телефона и описание через пробел.\
        \nНапример: Иванов Иван 12345 рабочий\n').split()
    data.append({'Фамилия': last_name, 'Имя': name, 'Телефон': phone, 'Описание': descr})



