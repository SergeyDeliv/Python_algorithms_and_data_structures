# Задача:
#  Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#  Количество элементов (n) вводится с клавиатуры.

# Первый вариант
n = int(input('Введите количество элементов: '))
i = 0
number = 1
sum_number = 0
while i < n:
    sum_number += number
    number /= -2
    i += 1

print(f'Сумма {sum_number}')

# Второй вариант


def sum_number1(h):
    s, a = 0.0, 1.0
    for _ in range(h):
        s += a
        a *= -0.5
    return f'Сумма {s}'


print(sum_number1(int(input('Введите количество элементов: '))))
