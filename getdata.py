def get_data():
    with open('file.txt', 'r', encoding="utf-8") as file:
        name, phone, action = file.readline().split(';')
        return (name, phone, action)  # Нужен картеж
