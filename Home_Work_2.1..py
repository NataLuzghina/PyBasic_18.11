# Задача № 1
n = int(input('Введите количество школьников:'))
k = int(input('Введите количество яблок:'))
print(f'Количество яблок для каждого школьника: {k // n}')
print(f'Количество яблок для каждого школьника: {k % n}')

# Задача № 2
class_1 = int(input('Введите количество школьников:'))
class_2 = int(input('Введите количество школьников:'))
class_3 = int(input('Введите количество школьников:'))
print(f'Количество парт для всех учеников: {(((class_1 // 2) + (class_1 % 2)) + ((class_2 // 2) + (class_2 % 2)) + ((class_3 // 2) + (class_3 % 2)))}')

# Задача № 3
number = int(input('ВВедите трехзначное число:'))
print (f'{number % 10}{number // 10 % 10}{number // 100 % 10}')

# Задача № 4
sek = int(input('ВВедите количество секунд:'))
print(f'В этом количестве секунд {sek // 3600}часов:{sek % 3600 // 60}минут:{sek % 60}секунд')


