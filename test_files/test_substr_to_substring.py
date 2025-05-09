import pytest
from SUBSTR_SUBSTRING import subtstr_to_substring  # Убедитесь, что импортируете вашу функцию правильно

def test_substr_with_length():
    sql_query = "SELECT SUBSTR(name, 1, 5) FROM users;"
    expected_result = "SELECT SUBSTRING(name FROM 1 FOR 5) FROM users;"
    assert subtstr_to_substring(sql_query) == expected_result

def test_substr_without_length():
    sql_query = "SELECT SUBSTR(name, 3) FROM users;"
    expected_result = "SELECT SUBSTRING(name FROM 3) FROM users;"
    assert subtstr_to_substring(sql_query) == expected_result

def test_substr_with_condition():
    sql_query = "SELECT SUBSTR(name, 2, 10) FROM users WHERE age > 30;"
    expected_result = "SELECT SUBSTRING(name FROM 2 FOR 10) FROM users WHERE age > 30;"
    assert subtstr_to_substring(sql_query) == expected_result

def test_multiple_substr():
    sql_query = "SELECT SUBSTR(name, 0, 5), SUBSTR(description, 3, 15) FROM products;"
    expected_result = "SELECT SUBSTRING(name FROM 0 FOR 5), SUBSTRING(description FROM 3 FOR 15) FROM products;"
    assert subtstr_to_substring(sql_query) == expected_result

def test_substr_edge_case_empty_string():
    sql_query = "SELECT SUBSTR(text, 1, 3) FROM logs;"
    expected_result = "SELECT SUBSTRING(text FROM 1 FOR 3) FROM logs;"
    assert subtstr_to_substring(sql_query) == expected_result

def test_substr_invalid_syntax():
    sql_query = "SELECT SUBSTR(text 1 3) FROM logs;"  # Некорректный SQL
    expected_result = sql_query  # Функция не должна ничего менять
    assert subtstr_to_substring(sql_query) == expected_result