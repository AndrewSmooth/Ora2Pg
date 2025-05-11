import pytest
from cast import number_to_cast

def test_simple_to_number():
    oracle_sql = "SELECT TO_NUMBER(col1) FROM table1;"
    expected_result = "SELECT CAST(col1 AS NUMERIC) FROM table1;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_with_spaces():
    oracle_sql = "SELECT TO_NUMBER( col2 ) FROM table2;"
    expected_result = "SELECT CAST(col2 AS NUMERIC) FROM table2;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_with_string_literal():
    oracle_sql = "SELECT TO_NUMBER('111') FROM test"
    expected_result = "SELECT CAST('111' AS NUMERIC) FROM test"
    assert number_to_cast(oracle_sql) == expected_result

def test_invalid_to_number_syntax():
    oracle_sql = "SELECT TO_NUMBER('123' FROM dual;"
    expected_result = "SELECT TO_NUMBER('123' FROM dual;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_in_subquery():
    oracle_sql = "SELECT id FROM (SELECT TO_NUMBER(salary) FROM employees) sub;"
    expected_result = "SELECT id FROM (SELECT CAST(salary AS NUMERIC) FROM employees) sub;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_with_expression():
    oracle_sql = "SELECT TO_NUMBER(col1 + col2) FROM table5;"
    expected_result = "SELECT CAST(col1 + col2 AS NUMERIC) FROM table5;"
    assert number_to_cast(oracle_sql) == expected_result

def test_multiple_to_number_calls():
    oracle_sql = "SELECT to_number('123'), To_Number(col), TO_number(col) FROM dual;"
    expected_result = "SELECT CAST('123' AS NUMERIC), CAST(col AS NUMERIC), CAST(col AS NUMERIC) FROM dual;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_in_string_literal():
    oracle_sql = "SELECT 'Call TO_NUMBER here' AS message;"
    expected_result = "SELECT 'Call TO_NUMBER here' AS message;"
    assert number_to_cast(oracle_sql) == expected_result

def test_multiple_to_number_different_args():
    oracle_sql = "SELECT TO_NUMBER(col1), TO_NUMBER('789') FROM table3;"
    expected_result = "SELECT CAST(col1 AS NUMERIC), CAST('789' AS NUMERIC) FROM table3;"
    assert number_to_cast(oracle_sql) == expected_result

def test_to_number_with_function_call():
    oracle_sql = "SELECT TO_NUMBER(SUBSTR(col, 1, 3)) FROM table4;"
    expected_result = "SELECT CAST(SUBSTR(col, 1, 3) AS NUMERIC) FROM table4;"
    assert number_to_cast(oracle_sql) == expected_result