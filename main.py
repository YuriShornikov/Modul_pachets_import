from application.db.people import get_employees

from application.salary import calculate_salary

from datetime import date


if __name__ == '__main__':
    first = get_employees()
    calculate_salary(first)
    the_date = date.today()
    print(the_date)

