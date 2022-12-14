# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
print('Введите координаты точки A: ')
x1 = InputNumbers('X1: ')
y1 = InputNumbers('Y1: ')
print('Введите координаты точки B: ')
x2 = InputNumbers('X2: ')
y2 = InputNumbers('Y2: ')
dist = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
print(f'Расстояние между точками A({x1},{y1}) и B({x2},{y2}) = {dist}')