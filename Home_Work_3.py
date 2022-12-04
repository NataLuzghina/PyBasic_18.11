numbers_1 = int(input('ВВедите любое число:'))
numbers_2 = int(input('ВВедите любое число:'))
operator = input('ВВедите оператор:')
if operator  == '+':
    print(numbers_1 + numbers_2)
if operator  == '-':
        print(numbers_1 - numbers_2)
if operator == '*':
    print(numbers_1 * numbers_2)
elif operator == '**':
    print(numbers_1 ** numbers_2)
elif operator == '/':
    print(numbers_1 / numbers_2)
else:
    print('Ошибка')


