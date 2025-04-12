import pytest
from sysdate import convert_sysdate_to_current_date  # Импортируем функцию

# Тестируем замену "SYSDATE" на "CURRENT_DATE"
def test_basic_replacement():
    query = "SELECT * FROM users WHERE join_date = SYSDATE;"
    expected_result = "SELECT * FROM users WHERE join_date = CURRENT_DATE;"
    result = convert_sysdate_to_current_date(query)
    assert result == expected_result  # Проверка на правильность замены

# Тестируем замену "SYSDATE" на "CURRENT_DATE" в разных регистрах
def test_case_insensitive_replacement():
    query = "SELECT * FROM orders WHERE order_date = SySdAtE;"
    expected_result = "SELECT * FROM orders WHERE order_date = CURRENT_DATE;"
    result = convert_sysdate_to_current_date(query)
    assert result == expected_result

# Тестируем отсутствие изменений, если "SYSDATE" нет в запросе
def test_no_change_if_no_sysdate():
    query = "SELECT * FROM products WHERE product_id = 123;"
    expected_result = "SELECT * FROM products WHERE product_id = 123;"
    result = convert_sysdate_to_current_date(query)
    assert result == expected_result

# Тестируем множественные вхождения "SYSDATE"
def test_multiple_replacements():
    query = "SELECT * FROM employees WHERE hire_date = SYSDATE AND end_date = SYSDATE;"
    expected_result = "SELECT * FROM employees WHERE hire_date = CURRENT_DATE AND end_date = CURRENT_DATE;"
    result = convert_sysdate_to_current_date(query)
    assert result == expected_result

# Тестируем строку без SYSDATE
def test_empty_query():
    query = ""
    expected_result = ""
    result = convert_sysdate_to_current_date(query)
    assert result == expected_result
