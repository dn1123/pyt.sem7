'''
Модуль отвечает за логирование (logging, процесс записи информации)
Заносит в журнал все обращения за получением данных от оператора
'''

def surname_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('surname: {}; '.format(data))
# 'a' открыть для дозаписи в конец файла; если файла нет, то создаётся новый

def name_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('name: {}; '.format(data))

def phone_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('phone: {}; '.format(data))

def describtion_logger(data):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('describtion: {}.\n'.format(data))