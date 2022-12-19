# Реализуйте алгоритм перемешивания списка.
import random
def ShuffleList(number):
    for i in range(len(number)-1):  
        index_shuffle = random.randint(0, len(number)-1)
        temp = number[i]
        number[i] = number[index_shuffle]
        number[index_shuffle] = temp       
    return number

numbers = [11, 23, 32, 3, 5, 6, 7, 8]
print(f'Исходный список {numbers}')
shuffle_list = ShuffleList(numbers)
print(f'Перемешанный список {shuffle_list}')