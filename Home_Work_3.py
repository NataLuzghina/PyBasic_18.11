number_1 = int(input('ВВедите любое число:'))
number_2 = int(input('ВВедите любое число:'))
operator = input('ВВедите оператор:')
if operator == '+':
    print(number_1 + number_2)
elif operator == '-':
    print(number_1 - number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == '**':
    print(number_1 ** number_2)
elif operator == '/':
    print(number_1 / number_2)
else:
    print('Какая-то ошибка')


