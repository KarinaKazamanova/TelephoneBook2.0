import csv 

def writing_down_csv(book: dict):
    with open('names.csv', 'w', newline='') as csvfile:
        for k, v in book.items():
            csvfile.writelines(f"{k}; {v}", sep= '\n')
            


def writing_down_txt(book: dict):
    with open('telephonebook.txt', 'w', encoding="utf-8") as file:
        for k, v in book.items():
            file.writelines(f"{k}; {v}\n")



def writing_down(format, book: dict):
    if format == 'txt':
        writing_down_txt(book)
    elif format == 'csv':
        writing_down_csv(book)