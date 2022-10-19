# read from file
def read_csv(phone_book: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(phone_book, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

# write in file.txt
# "5. Сохранить справочник в текстовом формате\n"
def write_in_file(phone_book, data):
    with open(phone_book, 'w', encoding='utf-8') as f:
        for dict in data:
            for v in dict:
                f.write(f'{dict[v]}\n\n')
