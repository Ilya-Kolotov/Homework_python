import validator, os

def view_data(data):
    print(data)

def get_value(text):
    result = input(text)
    while len(result) == 0:
        print('Поле не должно быть пустым. Введите значение: ')
        result = input()
    return result

def get_value_number(text):
    result = input(text)
    while not validator.is_num(result):
        print('Нужно ввести число. Попробуйте снова: ')
        result = input()
    return int(result)

def get_mode(text):
    modes = ['1', '2', '3']
    mode = input(text)
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)

def get_mode_import(text):
    modes = ['1', '2']
    mode = input(text)
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)
