# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
def ListNElem(number):
    if number > 0:
        number = list(range(-numN, numN+1))
    else:
        number = list(range(-numN, numN-1, -1))
    return number
def ProductElemOnPosition(number):    
    path = 'file.txt'
    data = open(path, 'r')
    product = 1
    for line in data:
        a= int(line)
        product *= number[a]
    data.close()
    return product

numN = InputNumbers('Введите число N: ')
number = ListNElem(numN)
print(number)
product = ProductElemOnPosition(number)
print(f'Произведение элементов на указанных позициях = {product}')


