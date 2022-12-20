# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
def dec_to_bin(number):
    binNumber = 0
    d10 = 1
    while (number > 0):
        binNumber = binNumber + number % 2 * d10
        number //= 2
        d10 *= 10
    return binNumber

num = InputNumbers('Введите число: ')
binNumber = dec_to_bin(num)
print(f'Число {num} в двоичной системе = {binNumber}')