# https://drive.google.com/file/d/1XC2qfTSjUTaDIGcxi-dElxO0RXsbX8C5/view?usp=sharing

# Задача:
#  Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
#  Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
#  а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
#  в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
#  программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать
#  пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    sym = input("Введите действие  '0', '+', '-', '*', '/' (0 для выхода): ")
    if sym == '+' or sym == '-' or sym == '*' or sym == '/':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if sym == '+':
            print(f'Сумма чисел {a} и {b} равна {a + b}')
        elif sym == '-':
            print(f'Разность чисел {a} и {b} равна {a - b}')
        elif sym == '*':
            print(f'Произведение чисел {a} и {b} равна {a * b}')
        elif sym == '/':
            print("%s" % (f'Частное чисел {a} и {b} равна {int(a / b)}' if b != 0 else 'На ноль делить нельзя'))
    elif sym == '0':
        break
    else:
        print('Введено неверное число')
