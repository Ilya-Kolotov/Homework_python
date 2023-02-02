import view, export_data

def button():
    mode = view.get_mode()
    if mode == 1:
        student = view.get_value('Введите Имя, Фамилию: ')
        export_data.init_students(student)
        export_data.write_data_student()
        button()
    elif mode == 2:
        item = view.get_value('Введите название предмета: ')
        export_data.init_items(item)
        export_data.write_data_item()
        button()
    elif mode == 3:
        for indx, val in enumerate(export_data.result_student):
            print(indx + 1, val)
        check_student = view.get_value_number('Выберите порядковый номер студента - ')
        for indx, val in enumerate(export_data.lessons):
            print(indx + 1, val)
        check_item = view.get_value_number('Выберите порядковый номер предмета - ')
        grade = view.get_value_number('Поставить оценку: ')
        export_data.write_data_grade(check_student, check_item, grade)

        button()
    elif mode == 4:
        export_data.output_data()
        button()
    elif mode == 5:
        for indx, val in enumerate(export_data.result_student):
            print(indx + 1, val)
        check_student = view.get_value_number('Выберите порядковый номер студента - ')
        export_data.output_student_grade(check_student)
        button()
    else:
        return print('Программа завершена')