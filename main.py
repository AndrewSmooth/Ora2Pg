# Это главный файл проекта. Здесь будет обработка самого sql-файла с помощью функций из других файлов.
# Пока написал ориентировочно функционал, который тут должен быть

# импорт функций из файлов с кейсами

from example_number_to_numeric import number_to_numeric

filename = "oracle.sql"

with open (filename, "r") as sql_file:
    sql_text = sql_file.read()
    print(sql_text) # до изменений
    sql_text = number_to_numeric(sql_text) # изменение sql_text с помощью импортированных функций
    print(sql_text) # после изменений

with open("postgres.sql", "w") as new_file:
    new_file.write(sql_text)