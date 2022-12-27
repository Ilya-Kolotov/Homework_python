# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            if number > 0:
                is_OK = True
            else:
                print('Ошибка! Введите неотрицательное число')
        except ValueError:
            print('Ошибка! Введите число')
    return number

def multi_number(number):
    spisok = []
    i = 2
    while i <= number:
        if number % i == 0:
            spisok.append(i)
            number = number // i
        else:
            i += 1
    if len(spisok) == 1:
        spisok.insert(0, 1)
    return spisok
num = InputNumbers('Введите число: ')

a = multi_number(num)
print(f'Число N = {num} имеет следующие простые множители - ', ', '.join(map(str, a)))
