import pytest
from interval0_0 import to_interval

def test_dsinterval_simple_days():
    oracle_sql = "SELECT to_DSINTERVAL('5') AS d FROM dual;"
    expected_result = "SELECT INTERVAL '5 days' AS d FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_dsinterval_case_insensitive():
    oracle_sql = "SELECT TO_dsinterval('5') AS d FROM dual;"
    expected_result = "SELECT INTERVAL '5 days' AS d FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_yminterval_zero():
    oracle_sql = "SELECT TO_YMINTERVAL('0-0') FROM dual;"
    expected_result = "SELECT INTERVAL '0 months' FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_multiple_dsintervals():
    oracle_sql = """SELECT
TO_DSINTERVAL('03:00:00') AS time,
TO_DSINTERVAL('7') AS days,
TO_DSINTERVAL('0 00:00:00')
FROM dual;"""
    expected_result = """SELECT
INTERVAL '0 days 03:00:00' AS time,
INTERVAL '7 days' AS days,
INTERVAL '0 days 00:00:00'
FROM dual;"""
    assert to_interval(oracle_sql) == expected_result

def test_yminterval_years_months():
    oracle_sql = "SELECT TO_YMINTERVAL('02-06') FROM dual;"
    expected_result = "SELECT INTERVAL '2 years 6 months' FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_dsinterval_with_spaces():
    oracle_sql = "SELECT TO_DSINTERVAL(' 10 04:00:00 ')"
    expected_result = "SELECT INTERVAL '10 days 04:00:00'"
    assert to_interval(oracle_sql) == expected_result

def test_dsinterval_zero_time():
    oracle_sql = "SELECT TO_DSINTERVAL('0 00:00:00') FROM dual;"
    expected_result = "SELECT INTERVAL '0 days 00:00:00' FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_dsinterval_days_and_time():
    oracle_sql = "SELECT TO_DSINTERVAL('5 12:30:45') FROM dual;"
    expected_result = "SELECT INTERVAL '5 days 12:30:45' FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_yminterval_with_alias():
    oracle_sql = "SELECT TO_YMINTERVAL('1-2') AS ym FROM dual;"
    expected_result = "SELECT INTERVAL '1 years 2 months' AS ym FROM dual;"
    assert to_interval(oracle_sql) == expected_result

def test_dsinterval_with_alias():
    oracle_sql = "SELECT TO_DSINTERVAL('4 02:00:00') AS full FROM dual;"
    expected_result = "SELECT INTERVAL '4 days 02:00:00' AS full FROM dual;"
    assert to_interval(oracle_sql) == expected_result