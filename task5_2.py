# Задание №2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

a = input("Введите первое 16-ое число: ").upper()  # 'A2'
b = input("Введите второе 16-ое число: ").upper()  # 'C4F'
HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
result = deque()


def sum_hex(x, y):
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer
        else:
            res = HEX_NUM[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return result


print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
