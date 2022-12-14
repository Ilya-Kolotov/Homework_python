# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
num = InputNumbers('Введите номер четверти от 1 до 4: ')
if num in range(1, 5):
    if num == 1:
        print('Диапазон координат точек равен (x > 0, y > 0)')
    elif num == 2:
        print('Диапазон координат точек равен (x < 0, y > 0)')
    elif num == 3:
        print('Диапазон координат точек равен (x < 0, y < 0)')
    elif num == 4:
        print('Диапазон координат точек равен (x > 0, y < 0)')
else:
    print('Введено некорректное число')