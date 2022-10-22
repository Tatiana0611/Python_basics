# show menu
def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Показать всех сотрудников")
    print("2. Найти сотрудника")
    print("3. Сделать выборку сотрудников по должности")
    print("4. Сделать выборку сотрудников по зарплате")
    print("5. Добавить сотрудника")
    print("6. Удалить сотрудника")
    print("7. Обновить данные сотрудника")
    print("8. Экспортировать данные в формате json")
    print("9 Экспортировать данные в формате csv")
    print("10. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# enter search value
def find_value(title):    
    return input(f'Введите {title} сотрудника: ')

# # show all employees
# # "1. Показать всех сотрудников"
def show_employees(data):
    for dict in data:
        print(' '.join(f'{k}' for k in dict.values()))

# find employee by id, last_name or first_name
# "2. Найти сотрудника"
def find_person(data, find_value):
    for dict in data:
        if dict['id'] == find_value or dict['last_name'] == find_value or dict['first_name'] == find_value:
            find_person = ' '.join(f'{k}' for k in dict.values())
            print(f'{find_person}')
    if not any(dict for dict in data if dict['id'] == find_value or dict['last_name'] == find_value or dict['first_name'] == find_value):
        print('Такого сотрудника нет')

# find employee by position
# "3. Сделать выборку сотрудников по должности"
def find_position(data, find_value):
    for dict in data:
        if dict['position'] == find_value:
            find_person = ' '.join(f'{k}' for k in dict.values())
            print(f'{find_person}')
    if not any(dict for dict in data if dict['position'] == find_value):
        print('Такого сотрудника нет')

# find employee by salary
# "4. Сделать выборку сотрудников по зарплате"
def find_salary(data, find_value):
    for dict in data:
        if dict['salary'] == int(find_value):
            find_person = ' '.join(f'{k}' for k in dict.values())
            print(f'{find_person}')
    if not any(dict for dict in data if dict['salary'] == int(find_value)):
        print('Такого сотрудника нет')

# get employee
# "5. Добавить сотрудника"
def get_person():
    id, last_name, first_name, position, salary = input('Для добавления сотрудника введите его ID, фамилию, имя, должность, зарплату через пробел.\
        \nНапример: 1 Иванов Иван водитель 40000\n').split()
    return {'id': id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'salary': int(salary)}

# get new information about employee
# "7. Обновить данные сотрудника"
def get_new_info():
    id, last_name, first_name, position, salary = input('Введите через пробел измененные данные сотрудника: ID, фамилию, имя, должность, зарплату\
        \nНапример: 1 Иванов Иван водитель 40000\n').split()
    return {'id': id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'salary': int(salary)}


