# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

new_company = namedtuple('new_company', 'name profit')
comanys = []
cnt = int(input('Введите количество предприятий = '))
sum_ = 0

for i in range(cnt):
    comanys.append(new_company(input(f'{i + 1}. Введите название = '), int(input(f'{i + 1}. Введите прибыль = '))))
    sum_ += comanys[i].profit

avg_ = sum_ / cnt

great_= []
less_ = []

for el in comanys:
    if el.profit > avg_:
        great_.append(el.name)
    elif el.profit < avg_:
        less_.append(el.name)

# print(comanys)
print(f'Средняя прибыль = {round(avg_, 2):.2f}')
print('Компании с прибылью меньше среднего: ' + ', '.join(less_))
print('Компании с прибылью больше среднего: ' + ', '.join(great_))