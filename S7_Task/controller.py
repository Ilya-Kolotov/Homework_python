import view, export_data, import_data

def button():
    mode = view.get_mode()
    while mode == 1:
        id = view.get_value_number('Введите Id отрудника: ')
        lastname = view.get_value('Введите Фамилию: ')
        name = view.get_value('Введите имя: ')
        phone = view.get_value_number('Введите телефон: ')
        comment = view.get_value('Введите комментарий: ')
        export_data.init(id, lastname, name, phone, comment)
        export_data.write_data()
        mode = view.get_mode()
    if mode == 2:
        mode_sorted = view.get_mode_sorted()
        if mode_sorted == 1:
            export_data.write_data_sorted_name()
            mode_import = view.get_mode_import()
            if mode_import == 1:
                import_data.import_data()
            else:
                import_data.import_data_lastname_name()
        else:
            export_data.write_data_sorted_id()
            mode_import = view.get_mode_import()
            if mode_import == 1:
                import_data.import_data()
            else:
                import_data.import_data_lastname_name()
    else:
        return
