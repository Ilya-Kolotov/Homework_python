# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def inputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
num = inputNumbers("Введите число - ")
degree = inputNumbers("Введите степень - ")
if degree == 0:
    pow_num = lambda x, y: 1
elif degree < 0:
    pow_num = lambda x, y: 1/x if y == 1 else 1/x * pow_num(x, y - 1)
else:
    pow_num = lambda x, y: x if y == 1 else x * pow_num(x, y - 1)

print(f"Число {num} в степени {degree} = {pow_num(num, abs(degree))}")