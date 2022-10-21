import csv 

def writing_down_csv(book: dict):
    with open('names.csv', 'w', newline='') as csvfile:
        for k, v in book.items():
            csvfile.writelines(f"{k}; {v}")
            csvfile.writelines('\n')


def writing_down_txt(book: dict):
    with open('telephonebook.txt', 'w', encoding="utf-8") as file:
        for k, v in book.items():
            file.writelines(f"{k}; {v}")
            file.writelines('\n')


def writing_down(format):
    if format == 'txt':
        writing_down_txt()
    elif format == 'csv':
        writing_down_csv()