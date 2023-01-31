
def calculate_salary(first):
    for employer, profession in first.items():
        if profession == 'Программист':
            salary = 120000
        elif profession == 'Менеджер':
            salary = 60000
        elif profession == 'Тестировщик':
            salary = 80000
        salary_dict = {profession: salary}
        info = {employer: salary_dict}
        print(info)
