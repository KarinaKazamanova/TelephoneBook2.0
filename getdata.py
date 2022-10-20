def get_data():
    with open('file.txt', 'r', encoding="utf-8") as file:
        name, phone, action = file.readline().split(';')
        return (name, phone, action)  # Нужен картеж

def get_book():
    with open('telephonebook.txt', 'r', encoding="utf-8") as tb:
        book = dict(tb.readline().split()) # Надо переделать
        return book