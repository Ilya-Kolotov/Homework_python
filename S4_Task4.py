# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
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
k = InputNumbers('Введите натуральную степень: ')
stroka = ''
for i in range(k, -1, -1):
    a = random.randint(0, 101)
    if a == 0:
        stroka = stroka + ''
    elif i == 0:
        stroka = stroka + str(f'{a}')
    else:
        stroka = stroka + str(f'{a}*x^{i} + ')
stroka = stroka + ' = 0'

print(stroka)
data = open('S4_file.txt', 'w')
data.writelines(stroka)
data.close()