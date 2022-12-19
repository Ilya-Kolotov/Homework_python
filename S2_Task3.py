# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
def DictionarySeqNumbers(number):
    dictionary = {}
    for i in range(1, number +1):
        dictionary[i] = round((1+1/i)**i, 2)
    return dictionary
num = InputNumbers('Введите число: ')
seqNumbers = DictionarySeqNumbers(num)
print(f'Для n = {num} последовательность чисел -> {seqNumbers}')