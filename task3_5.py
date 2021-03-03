# Задание
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
index = -1
while i < len(array):
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

if array[index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент: {array[index]}. \n',
          f'Позиция в массиве {index + 1}')
