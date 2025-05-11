import pytest
from bin.2 import bin_to_num

def test_binary_digits_only():
    oracle_sql = "SELECT BIN_TO_NUM('1, 0, 1') FROM dual;"
    expected_result = "SELECT ('101'::bit(3))::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_non_binary_digits():
    oracle_sql = "SELECT BIN_TO_NUM('1, 0, A') FROM dual;"
    expected_result = "SELECT ('1' || '0' || 'A')::bit(3)::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_with_whitespace():
    oracle_sql = "SELECT BIN_TO_NUM(' 1 , 0 , 1 ') FROM dual;"
    expected_result = "SELECT ('101'::bit(3))::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_long_binary_sequence():
    oracle_sql = "SELECT BIN_TO_NUM('1, 0, 1, 1, 0, 1, 1, 1') FROM dual;"
    expected_result = "SELECT ('10110111'::bit(8))::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_empty_input():
    oracle_sql = "SELECT BIN_TO_NUM('') FROM dual;"
    expected_result = "SELECT (''::bit(1))::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_multiple_bin_to_num_calls():
    oracle_sql = "SELECT BIN_TO_NUM('1, 0') || BIN_TO_NUM('1, 1') FROM dual;"
    expected_result = "SELECT ('10'::bit(2))::integer || ('11'::bit(2))::integer FROM dual;"
    assert bin_to_num(oracle_sql) == expected_result

def test_with_tabs_and_spaces():
    oracle_sql = "SELECT BIN_TO_NUM( 1 , 0\t,\t1 ) AS res FROM dual"
    expected_result = "SELECT ('101'::bit(3))::integer AS res FROM dual"
    assert bin_to_num(oracle_sql) == expected_result

def test_with_column_expressions():
    oracle_sql = "SELECT BIN_TO_NUM(col1 + 1, col2) FROM t"
    expected_result = "SELECT (col1 + 1 || col2)::bit(2)::integer FROM t"
    assert bin_to_num(oracle_sql) == expected_result

def test_in_where_clause():
    oracle_sql = "SELECT * FROM t WHERE BIN_TO_NUM(f1, f2) > 2"
    expected_result = "SELECT * FROM t WHERE (f1 || f2)::bit(2)::integer > 2"
    assert bin_to_num(oracle_sql) == expected_result

def test_with_bitand_function():
    oracle_sql = "SELECT BITAND(BIN_TO_NUM(a, b, c), 3) AS masked FROM t"
    expected_result = "SELECT BITAND((a || b || c)::bit(3)::integer, 3) AS masked FROM t"
    assert bin_to_num(oracle_sql) == expected_result

def test_with_logical_operators():
    oracle_sql = "SELECT BIN_TO_NUM(flag1 AND flag2, flag3) FROM t"
    expected_result = "SELECT (flag1 AND flag2 || flag3)::bit(2)::integer FROM t"
    assert bin_to_num(oracle_sql) == expected_result


