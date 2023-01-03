def surname_txt(data):
    with open('dir.txt', 'a', encoding='utf-8') as file:
        file.write('surname: {};\n'.format(data))

def name_txt(data):
    with open('dir.txt', 'a', encoding='utf-8') as file:
        file.write('name: {};\n'.format(data))

def phone_txt(data):
    with open('dir.txt', 'a', encoding='utf-8') as file:
        file.write('phone: {};\n'.format(data))

def describtion_txt(data):
    with open('dir.txt', 'a', encoding='utf-8') as file:
        file.write('describtion: {}.\n\n'.format(data))