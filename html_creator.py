# описание HTML-генератора

from user_interface import surname_view
from user_interface import name_view
from user_interface import phone_view
from user_interface import describtion_view

def create(device = 1):
    style = 'style="font-size.30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>Surname: {}</p>\n'\
        .format(style, surname_view(device))
    html += '    <p {}>Name: {}</p>\n'\
        .format(style, name_view(device))
    html += '    <p {}>Phone: {}</p>\n'\
        .format(style, phone_view(device))
    html += '    <p {}>Describtion: {}</p>\n'\
        .format(style, describtion_view(device))
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html