import csv 
import init

# Считывание данных______________________________________

# Считывание данных txt
def get_name_txt():
    with open('file.txt', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        n = data[0]
        return n

def get_phone_txt():
    with open('file.txt', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        p = data[1]   
        return p

def get_action_txt():
    with open('file.txt', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        wtd = data[2]
        return wtd      



# Считывание данных csv
def get_name_csv():
    with open('file.csv', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        n = data[0]
        return n
        
def get_phone_csv():
    with open('file.csv', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        p = data[1]
        return p

def get_action_csv():
    with open('file.csv', 'r', encoding="utf-8") as file:
        data = [str(i) for i in file.readline().split(';')]
        wtd = data[2]
        return wtd



# Считывание данных по формату
def get_name(format):
    if format == 'txt':
       return get_name_txt()
    elif format == 'csv':
        return get_name_csv()

def get_phone(format):
    if format == 'txt':
       return get_phone_txt()
    elif format == 'csv':
        return get_phone_csv()

def get_action(format):
    if format == 'txt':
       return get_action_txt()
    elif format == 'csv':
        return get_action_csv()

#________________________________________________________


# Считывание телефонной книги____________________________


# Считывание телкниги txt
def get_book_txt():
    book = {}
    with open('telephonebook.txt', 'r', encoding="utf-8") as tb:
        data = [str(i) for i in tb.read().split(";")]
        book [data[0]] = data[1]
    return book
    


# Считывание телкниги csv
def get_book_csv():
    book = {}
    with open('telephonebook.csv', newline='', encoding="utf-8", errors='ignore') as csvfile:
        data = csv.reader(csvfile, delimiter=';', quotechar=';')
        for row in data:
            book[row[0]] = row[1]
        return book


# Считывание телкниги по формату
def get_book(format):
    if format == 'txt':
       return get_book_txt()
    elif format == 'csv':
        return get_book_csv()

#________________________________________________________


