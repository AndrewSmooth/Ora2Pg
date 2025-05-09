from functions.merge_to_delete_update_insert import merge_to_delete_update_insert
...

with open ("oracle_code.sql", "r") as sql_file: # Чтение oracle кода из файла
    postgres_code = sql_file.read()

    # Перевод кода с oracle на postgres
    postgres_code = merge_to_delete_update_insert(postgres_code) 
    ... 

with open("postgres_code.sql", "w") as new_file: # Сохранение нового кода в файл
    new_file.write(postgres_code)