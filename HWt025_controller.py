import HWt025_model as model
import HWt025_view as view

employees = model.read_csv()

def start_menu():
    while True:
        mode = view.get_mode()
        if mode == 1:
            search_key = model.get_key(view.get_search_key())
            search_empl = view.get_search_empl()
            found_empl = model.find_employee(employees, search_key, search_empl)
            view.print_to_console_found_empl(found_empl)
        elif mode == 2:
            name_pos = view.get_search_by_position()
            list_empl_pos = model.get_list_empl_by_pos(employees, name_pos)
            view.print_to_console_celection(list_empl_pos)
        elif mode == 3:
            print("Здесь будет model.salsry_sampling")
            hi, lo = view.get_salary_range()
            list_empl_salary = model.find_employees_by_salary_range(employees, float(hi), float(lo))
            view.print_to_console_celection(list_empl_salary)
        elif mode == 4:
            print("Здесь будет model.add_employee")
        elif mode == 5:
            print("Здесь будет model.del_employee")
        elif mode == 6:
            print("Здесь будет model.update_employee")
        elif mode == 7:
            print("Здесь будет model.export_data_json")
        elif mode == 8:
            print("Здесь будет model.export_data_csv")
        elif mode == 9:
            print('Всего хорошего!')
            break
        print('\nДальше?')


