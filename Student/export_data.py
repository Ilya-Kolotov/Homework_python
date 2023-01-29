students = ''
items = ''
result_student = []
lessons = []
dict_students = {}

def init_students(student):
    global students
    students = student

def init_items(item):
    global items
    items = item

def write_data_student():
    global result_student
    global dict_students
    if students not in result_student:
        dict_students[students] = {}
        result_student.append(students)
        if lessons:
            for less in lessons:
                dict_students[students][less] = []



def write_data_item():
    global lessons
    lessons.append(items)
    for name in result_student:
        dict_students[name][items] = []


def write_data_grade(check_student, check_item, grade):
    # global result_grade
    for indx, val in enumerate(result_student):
        if indx == check_student - 1:
            check_stud = val
    for indx, val in enumerate(lessons):
        if indx == check_item - 1:
            check_less = val
    dict_students[check_stud][check_less].append(grade)

def output_data():
    for indx, val in enumerate(result_student):
        print(val)

def output_student_grade(check_student):
    for indx, val in enumerate(dict_students):
        if indx == check_student - 1:
            check_s = val
    for keys, val in dict_students.items():
        if keys == check_s:
            print(f'Фамилия Имя: {keys}')
            for key in lessons:
                print(f'Предмет: {key} , Оценки -',' '.join(map(str, dict_students[keys][key])))
# init_students('HH')
# write_data_student()
# output_data()