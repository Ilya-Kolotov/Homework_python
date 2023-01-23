# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# import  itertools
# def convert_stroka(str):
#     polyn = str.replace('= 0', '')
#     polyn = polyn.replace('^', ' ')
#     polyn = polyn.replace('*', ' ')
#     polyn = polyn.split('+')
#     polyn = [char.split(' ') for char in polyn]
#     polyn = [[x for x in list if x] for list in polyn]
#     for i in polyn:
#             if i[0] == 'x': i.insert(0, 1)
#             if i[-1] == 'x': i.append(1)
#             if len(i) == 1: i.append(0)
#     polyn = [tuple(int(x) for x in j if x != 'x') for j in polyn]
#     return polyn
# def fold_polyns(pol1, pol2):
#     if pol1[0][1] < pol2[0][1]:
#         x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     else:
#         x = [0] * (max(pol2[0][1], pol1[0][1] + 1))
#     for i in pol1 + pol2:
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res
# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0':
#             del (x[0])
#         if x[-1] == '0':
#             del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
#             del (x[0])
#             x[0] = x[0][1:]
#         if len(x) > 1 and x[-1] == '1':
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))
#
# data1 = open('file1.txt', 'r')
# data2 = open('file2.txt', 'r')
# stroka1 = data1.read()
# stroka2 = data2.read()
# data1.close()
# data2.close()
# print(stroka1)
# print(stroka2)
# polyn1 = convert_stroka(stroka1)
# polyn2 = convert_stroka(stroka2)
# fold_polyns = fold_polyns(polyn1, polyn2)
# sum_polyn = get_sum_pol(fold_polyns)
# print(sum_polyn)
# data = open('S4_file_Sum.txt', 'w')
# data.writelines(sum_polyn)
# data.close()

pol1 = "12*x**8+2*x**6+2*x**4+3*x**3+2*x**2"
pol2 = "34*x**25+20*x**11+10*x**7+8*x**4+1*x**3+6*x**1+3"

pol1 = pol1.split("+")
pol2 = pol2.split("+")

print(pol1)
print(pol2)

for indx,value in enumerate(pol1):
    pol1[indx] = list(map(int,value.split("*x**")))
for indx,value in enumerate(pol2):
    pol2[indx] = list(map(int,value.split("*x**")))

print(pol1)
print(pol2)

result = pol1 + pol2
print(result)

result = sorted(result,key = lambda x: x[1] if len(x)>1 else 0,reverse=True)

print(result)
cur_indx = 0
result_list = []
while cur_indx<len(result)-1:
    cur_num = result[cur_indx]
    next_num = result[cur_indx+1]
    if len(cur_num)>1 and len(next_num)>1:
        if cur_num[1] == next_num[1]:
            sum_koeff = cur_num[0]+next_num[0]
            result_list.append([sum_koeff,cur_num[1]])
            cur_indx+=1
        else:
            result_list.append(result[cur_indx])
    elif len(cur_num)>1 and len(next_num) == 1:
        result_list.append(result[cur_indx])
    elif len(cur_num) == 1 and len(next_num) == 1:
        result_list.append([cur_num[0]+next_num[0]])
        cur_indx +=1
    cur_indx+=1

if cur_indx < len(result):
    result_list.append(result[-1])

print(result_list)

for indx,val in enumerate(result_list):
    if len(val)>1:
        result_list[indx] = f'{val[0]}*x**{val[1]}'
    else:
        result_list[indx] = f'{val[0]}'
print(result_list)
result_string = "+".join(result_list)
# print(result_string)



