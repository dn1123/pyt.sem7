import html_creator as hc # as для краткой записи, не обязательно

while True:
    print('Выберите режим работы со справочником: ')
    print('1. Импорт данных\n2. Экспорт данных из csv\n3. Экспорт данных из txt\n4. Выход из программы')
    mode = int(input())
    if mode == 1:
        hc.create()
    
    elif mode == 2:
        fd = open('log.csv', encoding='utf-8')
        print(fd.read())

    elif mode == 3:
        fd = open('dir.txt', encoding='utf-8')
        print(fd.read())

    elif mode == 4:
        print('Выход из программы')
        break