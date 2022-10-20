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
    t_book = gd.get_book()
    if n[0] not in t_book:
        note = (n[0], n, p)
        t_book = dict(note)
    return t_book
name, phone, what_to_do = gd.get_data()
# n, p, wtd = init(name, phone, what_to_do)
t_book = add_new_contact(name, phone)
print(t_book)

note = add_new_contact(name, phone)
print(note, name[0])