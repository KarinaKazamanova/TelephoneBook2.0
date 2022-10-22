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
   


def add_new_contact(n, p, format):
    t_book = gd.get_book(format)
    t_book[n] = p
    return t_book


def delete_contact(n, format):
    t_book = gd.get_book(format)
    del t_book[n]
    return t_book

def add_new_phone(n, p, format):
    t_book = gd.get_book(format)
    t_book[n] = str(t_book[n]) + " / " + str(p)
    return t_book


def update_contact(n, p, format):
    t_book = gd.get_book(format)
    t_book[n] = p
    return t_book

def action(wtd, n, p, format):
    if wtd == 'новый контакт':
        return add_new_contact(n, p, format)
    elif wtd == 'удаление контакта':
        return delete_contact(n, format)
    elif wtd == 'обновление номера':
        return update_contact(n, p, format)
    elif wtd == 'добавление номера':
        return add_new_phone(n, p, format)

