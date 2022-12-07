number_1 = float(input('Введите любое число:'))
number_2 = float(input('Введите любое число:'))
operator = input('Введите оператор:')
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
N = int(input('Введите число:'))
for i in range(1, N):
    if N >= i ** 2:
       print(i ** 2, end=' ')
print()
number = int(input('Введите число:'))
if number == 2 or number == 3:
    print('Простое')
if number % 2 != 0 and number % 3 != 0:
    print('Простое')
else:
     print('Сложное')
