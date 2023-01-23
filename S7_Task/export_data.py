ids = ''
names = ''
lastnames = ''
phones = ''
comments = ''

def init(id, lastname, name, phone, comment):
    global ids
    global names
    global lastnames
    global phones
    global comments
    ids = id
    names = name
    lastnames = lastname
    phones = phone
    comments = comment

def write_data():
    file = open('./user.csv', 'a', encoding='utf-8')
    result = f'{ids};{lastnames};{names};{phones};{comments}\n'
    file.write(result)
    file.close()


def write_data_sorted_id():
    file = open('./user.csv', 'r', encoding='utf-8')
    result = file.read()
    result = result.split('\n')
    for indx, val in enumerate(result):
        result[indx] = list(map(str, val.split(";")))
    del result[-1]
    result = sorted(result, key=lambda x: int(x[0]))
    file1 = open('./user_sorted.csv', 'w', encoding='utf-8')
    for indx, val in enumerate(result):
        result[indx] = ';'.join(val)
    for i in range(len(result)):
        file1.write(f'{result[i]}\n')
    file.close()
    file1.close()
def write_data_sorted_name():
    file = open('./user.csv', 'r', encoding='utf-8')
    result = file.read()
    result = result.split('\n')
    for indx, val in enumerate(result):
        result[indx] = list(map(str, val.split(";")))
    del result[-1]
    result = sorted(result, key=lambda x: x[2])
    file1 = open('./user_sorted.csv', 'w', encoding='utf-8')
    for indx, val in enumerate(result):
        result[indx] = ';'.join(val)
    for i in range(len(result)):
        file1.write(f'{result[i]}\n')
    file.close()
    file1.close()
