

profession_employees = {}

def get_employees():
    global profession_employees
    name = input('Введите имя сотрудника: ')
    surname = input('Введите фамилию сотрудника: ')
    employer = name + ' ' + surname
    profession = input('Назначить должность сотруднику Программист/Менеджер/Тестировщик: ')
    if profession == 'Программист' or profession == 'Менеджер' or profession == 'Тестировщик':
        profession_employees = {employer: profession}
        print('Сотрудник назначен')
        return profession_employees
    else:
        profession_employees = {}
        print('Сотрудник аутсайдер  - уволен')
        return profession_employees
