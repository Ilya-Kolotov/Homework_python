import validator

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

def get_mode():
    modes = ['1', '2', '3', '4', '5', '6']
    mode = input('1 - Добавить студента\n2 - Добавить предмет'
                 '\n3 - Добавить оценку\n4 - Показать список студентов\n'
                 '5 - Показать оценки по ученику\n6 - Завершить программу\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)

def get_mode_import():
    modes = ['1', '2']
    mode = input('1 - Вывести все данные\n2 - Вывести только фамилию и имя\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)

def get_mode_sorted():
    modes = ['1', '2']
    mode = input('1 - Сортировать по имени\n2 - Сортировать по id\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)