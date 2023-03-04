from datetime import datetime

from colorama import init, Fore
from random import choice

import application


if __name__ == '__main__':
    init()
    employees = application.get_employees()
    print(datetime.now().strftime("%d.%m.%Y %H:%M"))
    print()
    for employee in employees:
        color = choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW])
        print(f'{color}{application.calculate_salary(employee)}')
        
