# https://drive.google.com/file/d/1MGlTAchnDGxCA543hPLEKD2JxGVygLih/view?usp=sharing

# Задача:
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трёхзначное число: '))

a = n // 100
b = n % 100 // 10
c = n % 10
print(f'Сумма = {a + b + c}')
print(f'Произведение = {a * b * c}')
