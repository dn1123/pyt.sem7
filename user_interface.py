# модуль содержит три кнопки-метода для пользователя

import data_provider as prov
import logger as log
import txt_creator as tc

def surname_view(operator):
    data = prov.get_surname(operator) # получение данных
    log.surname_logger(data) # запись полученного значения
    tc.surname_txt(data)
    return data

def name_view(operator):
    data = prov.get_name(operator)
    log.name_logger(data)
    tc.name_txt(data)
    return data

def phone_view(operator):
    data = prov.get_phone(operator)
    log.phone_logger(data)
    tc.phone_txt(data)
    return data

def describtion_view(operator):
    data = prov.get_describtion(operator)
    log.describtion_logger(data)
    tc.describtion_txt(data)
    return data