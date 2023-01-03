# модуль поставляет данные

def get_surname(operator):
    if operator:
        return input('Введите фамилию человека: ')

def get_name(operator):
    if operator:
        return input('Введите имя человека: ')

def get_phone(operator):
    if operator:
        return input('Введите его телефон: ')

def get_describtion(operator):
    if operator:
        return input('Где используется телефон: ')

def data_collection(operator):
    return (get_surname(operator), get_name(operator), get_phone(operator), get_describtion(operator))