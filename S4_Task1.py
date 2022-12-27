# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}
import math
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            if number >= 0:
                is_OK = True
            else:
                print('Ошибка! Введите неотрицательное число')
        except ValueError:
            print('Ошибка! Введите число')
    return number
d = InputNumbers('Введите количество знаков после запятой в диапозоне от 1 до 10: ')
if d > 0 and d <= 10:
    print(f'При заданной точности d = {(10 ** -d):.{d}f}, число пи = {round(math.pi, d)}')
else:
    print('Введено неверное число')
