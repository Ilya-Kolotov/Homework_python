# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
def sum_numbers_odd_position(list):
    sum = 0
    for i in range(1, len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum
num = InputNumbers('Введите длину списка: ')
new_list = create_list(num)
print(new_list)
sum_odd = sum_numbers_odd_position(new_list)
print(f'Сумма элементов на нечетных позициях = {sum_odd}')