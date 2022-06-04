from application.people import get_employees
from application.salary import calculate_salary
import datetime

if __name__ == '__main__':
    print(get_employees(), datetime.date.today())
    print(calculate_salary(), datetime.date.today())