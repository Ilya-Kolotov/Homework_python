# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
num = InputNumbers('Введите число от 1 до 7: ')
if num in range(1,6):
    print('День не является выходным')
elif num == 6 or num == 7:
    print('День является выходным')
else:
    print('Введено некорректное число')