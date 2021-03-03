# Задание
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

number = array[0]
number_of_repetitions = 1

for i in range(len(array) - 1):
    count = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            count += 1
    if count > number_of_repetitions:
        number_of_repetitions = count
        number = array[i]

if number_of_repetitions > 1:
    print(f'Число {number} встречается {number_of_repetitions} раз(а)')
else:
    print('Все элементы уникальны')


