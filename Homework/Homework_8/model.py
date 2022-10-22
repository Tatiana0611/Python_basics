import csv
import json
from pathlib import Path
import view

# read csv
def read_csv() -> list:
    data = []
    with open(Path.cwd() / 'Homework/Homework_8/employees.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp['id'] = row[0]
            temp['last_name'] = row[1]
            temp['first_name'] = row[2]
            temp['position'] = row[3]
            temp['salary'] = int(row[4])
            data.append(temp)
    return(data)

# add employee
# "5. Добавить сотрудника"
def add_persone(data, dict):
    return data.append(dict)

# delete employee
# "6. Удалить сотрудника"
def del_person(data, find_value):
    new_data = [dict for dict in data if find_value not in dict['id']]
    return new_data

# update employee
# "7. Обновить данные сотрудника"
def update_person(data, find_value):
    for dict in data:
        if dict['id'] == find_value:
            dict.update(view.get_new_info())
    return data

# write json
# "8. Экспортировать данные в формате json"
def write_json(data):
    with open(Path.cwd() / 'Homework/Homework_8/employees_out.json', 'w', encoding='utf-8') as fout:
        for employee in data:
            fout.write(json.dumps(employee) + '\n')

# write csv
# "9. Экспортировать данные в формате csv"
def write_csv(data):
    with open(Path.cwd() / 'Homework/Homework_8/employees_out.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in data:
            csv_writer.writerow(employee.values())