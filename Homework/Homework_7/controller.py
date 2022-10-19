import model
import view

def print_data():
    data = model.read_csv('phone_book.csv')
    step = 0
    while not step == 6:
        step = view.show_menu()
        if step == 1:
            view.show_phone_book(data)
        if step == 2:
            find_value = view.find_value('Фамилия')
            view.find_person(data, 'Фамилия', find_value)
        if step == 3:
            find_value = view.find_value('Номер телефона')
            view.find_person(data, 'Телефон', find_value)
        if step == 4:
            view.add_person(data)
        if step == 5:
            model.write_in_file('phone_book.txt', data)
    else:
        print('Работа со справочником завершена')
