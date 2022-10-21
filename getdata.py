import csv 

def get_data_txt():
    with open('file.txt', 'r', encoding="utf-8") as file:
        name, phone, what_to_do = file.readline().split(';')
        return (name, phone, what_to_do)  # Нужен картеж

def get_data_csv():
    with open('file.csv', 'r', encoding="utf-8") as file:
        name, phone, what_to_do = str(file.readline().split(';'))
        return (name, phone, what_to_do)


def get_book_txt():
    with open('telephonebook.txt', 'r', encoding="utf-8") as tb:
        book = {}
        data =  tb.read().split(";")
        book [data[0]] = data[1]
    return book


def get_book_csv():
    with open('telephonebook.csv', newline='', encoding="utf-8", errors='ignore') as csvfile:
        book = {}
        data = csv.reader(csvfile, delimiter=';', quotechar=';')
        for row in data:
            book[row[0]] = row[1]
        return book

def get_book(format):
    if format == 'txt':
       return get_book_txt()
    elif format == 'csv':
        return get_book_csv()


def get_data(format):
    if format == 'txt':
        return get_data_txt()
    elif format == 'csv':
        return get_data_csv()


