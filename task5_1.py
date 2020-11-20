# Задание №1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company = namedtuple('Company', ['q1', 'q2', 'q3', 'q4'])
number = int(input("Количество предприятий: "))
lst = {}
total_profit = ()

for i in range(number):
    company_name = input(str(i + 1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    lst[company_name] = company(q1=profit_q1, q2=profit_q2, q3=profit_q3, q4=profit_q4)

for name, profit in lst.items():
    total_profit += profit

profit_total = sum(total_profit) / len(lst)
print(f'Средняя прибыль за год для всех предприятий {profit_total}')

for name, profit in lst.items():
    if sum(profit) < profit_total:
        print(f'Предприятия, у которых прибыль ниже среднего: \n {name} - {sum(profit)}')
    elif sum(profit) > profit_total:
        print(f'Предприятия, у которых прибыль выше среднего: \n {name} - {sum(profit)}')

