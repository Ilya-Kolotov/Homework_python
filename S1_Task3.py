#  Напишите программу, которая принимает на вход координаты точки (X и Y), 
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#  Пример:
#  - x=34; y=-30 -> 4
#  - x=2; y=4-> 1
#  - x=-34; y=-30 -> 3

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

x = InputNumbers('Введите координату точки X: ')    
y = InputNumbers('Введите координату точки Y: ') 
if x !=0 and y !=0:
    if x > 0 and y > 0:
        print('Точка принадлежит 1 четверти плоскости')
    elif x < 0 and y > 0:
        print('Точка принадлежит 2 четверти плоскости')
    elif x < 0 and y < 0:
        print('Точка принадлежит 3 четверти плоскости')
    elif x > 0 and y < 0:
        print('Точка принадлежит 4 четверти плоскости')
    elif x == 0 and y == 0:
        print('Точка принадлежит началу координат')
else:
    if x == 0 and y == 0:
        print('Точка принадлежит началу координат')
    elif x == 0:
        print('Точка лежит на оси X')
    elif y == 0:
        print('Точка лежит на оси Y')