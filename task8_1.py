# Задание №1
# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

s = 'papa'


def search_strings(s):
    n = len(s)
    arr_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j + i])

            if k not in arr_str:
                arr_str.add(k)

    return len(arr_str)


print(f'Количество подстрок: {search_strings(s)}')
