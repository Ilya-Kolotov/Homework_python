def import_data():
    file = open('./user_sorted.csv', 'r', encoding='utf-8')
    result = file.read()
    result = result.split('\n')
    for indx, val in enumerate(result):
        result[indx] = list(map(str, val.split(";")))
    del result[-1]
    for i in range(len(result)):
        resul_list = result[i][0]
        for j in range(len(result[i]) - 1):
            resul_list += ' ' + result[i][j + 1]
        print(resul_list)
    file.close()


def import_data_lastname_name():
    file = open('./user_sorted.csv', 'r', encoding='utf-8')
    result = file.read()
    result = result.split('\n')

    for indx, val in enumerate(result):
        result[indx] = list(map(str, val.split(";")))
    del result[-1]
    for i in range(len(result)):
        print(result[i][1] + ' ' + result[i][2])
    file.close()

