# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

def ListFactorial(number):
    list = []
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
        list.append(factorial)
    return list
num = InputNumbers('Введите число: ')
listFactorial = ListFactorial(num)
print(f'N = {num}, тогда набор произведений чисел -> {listFactorial}')