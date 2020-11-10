# Задание
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив до изменения:\n {array}')

max_el = array[0]
min_el = array[0]
min_index = 0
max_index = 0

for k in range(1, len(array)):
    if array[k] > max_el:
        max_el = array[k]
        max_index = k
    elif array[k] < min_el:
        min_el = array[k]
        min_index = k

array[max_index], array[min_index] = array[min_index], array[max_index]

print(f'Массив после изменения:\n {array}')
print(f'Максимальное число массива: {max_el}')
print(f'Минимальное число массива: {min_el}')
