# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

def SumDigit(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum
num = InputNumbers('Введите вещественное число: ')
sumDigit = SumDigit(num)
print(f"Сумма цифр числа {num} = {sumDigit}")