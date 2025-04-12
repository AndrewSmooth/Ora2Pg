import pytest
from DECODE_to_CASE import decode_to_case

def test_simple_decode(): 
    oracle_sql = "SELECT DECODE(status, 1, 'active', 0, 'inactive') FROM users"
    expected_result = "SELECT CASE status\n\t\tWHEN 1 THEN 'active'\n\t\tWHEN 0 THEN 'inactive'\n\t\tELSE 'inactive'\n\tEND FROM users"
    assert decode_to_case(oracle_sql) == expected_result

def test_decode_with_column():
    oracle_sql = "SELECT DECODE(age, 18, 'adult', 0, 'child') FROM people"
    expected_result = "SELECT CASE age\n\t\tWHEN 18 THEN 'adult'\n\t\tWHEN 0 THEN 'child'\n\t\tELSE 'child'\n\tEND FROM people"
    assert decode_to_case(oracle_sql) == expected_result

def test_decode_without_decode():
    oracle_sql = "SELECT name, age FROM users"
    expected_result = "SELECT name, age FROM users"
    assert decode_to_case(oracle_sql) == expected_result

def test_decode_with_multiple_conditions():
    oracle_sql = "SELECT DECODE(status, 1, 'active', 0, 'inactive', 2, 'pending') FROM users"
    expected_result = "SELECT CASE status\n\t\tWHEN 1 THEN 'active'\n\t\tWHEN 0 THEN 'inactive'\n\t\tWHEN 2 THEN 'pending'\n\t\tELSE 'pending'\n\tEND FROM users"
    assert decode_to_case(oracle_sql) == expected_result