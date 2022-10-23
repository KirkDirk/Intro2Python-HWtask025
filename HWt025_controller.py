import HWt025_model as model
import HWt025_view as view

def start_menu():
    while True:
        mode = view.get_mode()
        if mode == 1:
            employees = model.read_csv()
            search_key = model.get_key(view.get_search_key())
            search_empl = view.get_search_empl()
            found_empl = model.find_employee(employees, search_key, search_empl)
            view.print_to_console_found_empl(found_empl)
        elif mode == 2:
            print("Здесь будет model.celection_position")
        elif mode == 3:
            print("Здесь будет model.salsry_sampling")
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

def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result

