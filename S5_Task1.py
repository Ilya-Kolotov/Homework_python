# Напишите программу, удаляющую из текста все слова, содержащие
# ""абв"".

data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)