import pytest
from position_vl import instr_to_position

def test_simple_instr_to_position():
    oracle_sql = "SELECT * FROM clients WHERE INSTR(phone, '+7') > 0;"
    expected_result = "SELECT * FROM clients WHERE POSITION('+7' IN phone) > 0;"
    assert instr_to_position(oracle_sql) == expected_result

def test_invalid_instr_syntax():
    oracle_sql = "SELECT INSTR(name, 'a' FROM users;"
    expected_result = "SELECT INSTR(name, 'a' FROM users;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_with_function_call():
    oracle_sql = "SELECT INSTR(LOWER(name), 'a') FROM users;"
    expected_result = "SELECT POSITION('a' IN LOWER(name)) FROM users;"
    assert instr_to_position(oracle_sql) == expected_result

def test_multiple_instr_calls():
    oracle_sql = "SELECT INSTR(col1, 'x'), INSTR(col2, 'y') FROM table1;"
    expected_result = "SELECT POSITION('x' IN col1), POSITION('y' IN col2) FROM table1;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_in_where_clause():
    oracle_sql = "SELECT * FROM users WHERE INSTR(email, '@') > 0;"
    expected_result = "SELECT * FROM users WHERE POSITION('@' IN email) > 0;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_with_literals():
    oracle_sql = "SELECT INSTR('INSTR', 'INSTR') AS Position;"
    expected_result = "SELECT POSITION('INSTR' IN 'INSTR') AS Position;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_with_number():
    oracle_sql = "SELECT INSTR('abc123', 1) FROM dual;"
    expected_result = "SELECT POSITION(1 IN 'abc123') FROM dual;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_with_substr():
    oracle_sql = "SELECT INSTR(SUBSTR(name, 1, 10), 'x') FROM employees;"
    expected_result = "SELECT POSITION('x' IN SUBSTR(name, 1, 10)) FROM employees;"
    assert instr_to_position(oracle_sql) == expected_result

def test_invalid_instr_missing_paren():
    oracle_sql = "SELECT INSTR(email, '@' FROM users;"
    expected_result = "SELECT INSTR(email, '@' FROM users;"
    assert instr_to_position(oracle_sql) == expected_result

def test_instr_in_subquery():
    oracle_sql = "SELECT * FROM (SELECT INSTR(email, '@') FROM users) sub;"
    expected_result = "SELECT * FROM (SELECT POSITION('@' IN email) FROM users) sub;"
    assert instr_to_position(oracle_sql) == expected_result

def test_three_instr_calls():
    oracle_sql = "SELECT INSTR(col1, 'x'), INSTR(col2, 'y'), INSTR(col3, 'z') FROM table1;"
    expected_result = "SELECT POSITION('x' IN col1), POSITION('y' IN col2), POSITION('z' IN col3) FROM table1;"
    assert instr_to_position(oracle_sql) == expected_result
