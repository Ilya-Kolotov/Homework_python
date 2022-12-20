# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number =int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
def create_list(num):
    list_num = []
    for i in range(num):
        a = float(round(random.uniform(1, 11), 2))
        list_num.append(a)
    return list_num
def frac(list):
    frac_list = []
    for i in range(len(list)):
        list[i] = str(list[i])
        a = list[i].split('.')[1]
        if len(a) == 1:
            k = int(a)*10
        else:
            k = int(a)
        frac_list.append(k)
    return frac_list

num = InputNumbers('Введите длину списка: ')
new_list = create_list(num)
print(new_list)
frac_list = frac(new_list)
print(f'Разница между максимальным и минимальным значением дроби = {(max(frac_list) - min(frac_list))}')