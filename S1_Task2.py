# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
print('X Y Z', end = '     ')
print('Проверка истинности каждого значения')
truthState = False
count = 0
for i in range(0, 2):
    for k in range(0, 2):
        for l in range(0, 2):
            if not (i or k or l) == ( not i and not k and not l):
                print(f'{i} {k} {l}', end = ' --> ')
                print(True)
                truthState = True
            else:
                print(f'{i} {k} {l}', end = ' --> ')
                print(False)
                truthState = False
                count += 1
if count == 0:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
else:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - не истинно')