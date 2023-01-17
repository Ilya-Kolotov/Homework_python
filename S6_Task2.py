# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
def inputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

print("Задайте диапозон")
num_min = inputNumbers("Введите минимум - ")
num_max = inputNumbers("Введите максимум - ")
a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(f"Заданный массив {a}")
b = list(map(lambda x: x[0], filter(lambda x: x[1] <= num_max and x[1] >=num_min, enumerate(a))))
print(f"Индексы элементов массива, значения которых принадлежат заданному диапазону = {b}")