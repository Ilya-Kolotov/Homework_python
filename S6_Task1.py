# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def inputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
first_elem = inputNumbers("Введите первый элемент - ")
d = inputNumbers("Введите разность - ")
num = inputNumbers("Введите количество элементов - ")

a = [first_elem + (i -1)*d for i in range(1, num+1)]
print(f"Первый элемент = {first_elem}, разность = {d}, количество элементов = {num}")
print(f"Арифметическая прогрессия = {' '.join(map(str, a))}")