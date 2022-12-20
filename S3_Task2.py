# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number


def create_list(num):
    list_num = []
    for i in range(num):
        a = random.randint(1, 11)
        list_num.append(a)
    return list_num


def multi_element(list):
    list_multi = []
    for i in range(len(list) // 2 + len(list) % 2):
        a = list[i] * list[-1 - i]
        list_multi.append(a)
    return list_multi


num = InputNumbers('Введите длину списка: ')
new_list = create_list(num)
print(new_list)
list_multi = multi_element(new_list)
print(f'Произведение пар чисел = {list_multi}')
