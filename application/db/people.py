

list_employees = []

def get_employees():
    global list_employees
    name = input('Введите имя сотрудника: ')
    surname = input('Введите фамилию сотрудника: ')
    list_employees.append(name + ' ' + surname)


get_employees()
print(list_employees)