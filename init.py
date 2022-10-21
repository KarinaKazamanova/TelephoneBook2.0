import getdata as gd

name = ''
phone = ''
what_to_do = ''

def init(n, p, wtd):
    global name
    global phone
    global what_to_do
    name = n
    phone = p
    what_to_do = wtd


def add_new_contact(n, p):
    t_book = gd.get_book('txt')
    t_book [n] = p
    return t_book


def delete_contact(n):
    t_book = gd.get_book('txt')
    del t_book[n]
    return t_book

def add_new_phone(n, p):
    t_book = gd.get_book('txt')
    t_book[n].append(p)
    return t_book


def update_contact(n, p):
    t_book = gd.get_book('txt')
    t_book [n] = p
    return t_book

def action(wtd, n, p):
    if wtd == 'новый контакт':
        add_new_contact(n, p)
    elif wtd == 'удаление контакта':
        delete_contact(n)
    elif wtd == 'обновление номера':
        update_contact(n, p)
    elif wtd == 'добавление номера':
        add_new_phone(n, p)

name, phone, what_to_do = gd.get_data_txt()
print(name)
print(phone)
print(what_to_do)