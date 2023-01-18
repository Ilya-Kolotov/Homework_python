# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEE
# Выходные данные:
# 6A1F2D7C1A5E

def encode(text):
    result = ""
    prev_char = text[0]
    count = 0
    for char in text:
        if char != prev_char:
            result += f"{count}{prev_char}"
            prev_char = char
            count = 1
        else:
            count +=1
    result += f"{count}{prev_char}"
    return result

def decode(text):
    result = ""
    count = ""
    digit = True
    for char in text:
        if digit:
            count = char
            digit = False
        else:
            result += int(count)*char
            digit = True
    return result

text = "11111222233444555555555"
print(f"Исходный текст {text}")
encode_text = encode(text)
print(f"Результат сжатия данных {encode_text}")
print(f"Результат восстановления данных {decode(encode_text)}")