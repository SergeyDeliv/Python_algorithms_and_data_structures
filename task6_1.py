# Задание №1
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Windows 10 Pro x64
# Python 3.8.2

import sys
import random

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])


min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
        'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
        min_list[0]
            )

sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(min_list)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size)

#############################################################################################################

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер листа', sys.getsizeof(r))
print('Размер элемента листа', sys.getsizeof(r[0]))
print('Размер кортежа', sys.getsizeof(tuple(r)))
print('Размер элемента кортежа', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('Размер всех элементов в листе', sum)

#############################################################################################################

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер листа', sys.getsizeof(r))
print('Размер элемента листа', sys.getsizeof(r[0]))
print('Размер кортежа', sys.getsizeof(tuple(r)))
print('Размер элемента кортежа', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('Размер всех элементов в листе', sum)


