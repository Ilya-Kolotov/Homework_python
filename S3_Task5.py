# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            if number >= 0:
                is_OK = True
            else:
                print('Ошибка! Введите неотрицательное число')
        except ValueError:
            print('Ошибка! Введите число')
    return number

def fib(num):
    if num == 0:
        return 0
    if num in [1, 2]:
        return 1
    else:
        return fib(num-1) + fib(num-2)
def fib_list(num):
    list = []
    for i in range(-num, num+1):
        if i < 0:
            list.append(int(((-1)**(i + 1))*fib(i*-1)))
        else:
            list.append(fib(i))
    return list
num = InputNumbers('Введите количество чисел последовательности Фибоначчи: ')
fibList = fib_list(num)
print(f'Для к = {num} список чисел Фибоначчи будет выглядеть так - > {fibList}')
