import model
import view

def print_data():
    data = model.read_csv()
    choice = 0
    while not choice == 10:
        choice = view.show_menu()
        if choice == 1:
            view.show_employees(data)
        elif choice == 2:
            find_value = view.find_value('ID, фамилию или имя')
            view.find_person(data, find_value)
        elif choice == 3:
            find_value = view.find_value('должность')
            view.find_position(data, find_value)
        elif choice == 4:
            find_value = view.find_value('зарплату')
            view.find_salary(data, find_value)
        elif choice == 5:
            model.add_persone(data, view.get_person())
        elif choice == 6:
            find_value = view.find_value('ID')
            data = model.del_person(data, find_value)
        elif choice == 7:
            find_value = view.find_value('ID')
            data = model.update_person(data, find_value)
        elif choice == 8:
            model.write_json(data)
        elif choice == 9:
            model.write_csv(data)
    else:
        print('Работа со справочником завершена')
