import pytest
from data_types import convert_data_types

def test_number_to_numeric_with_precision():
    oracle_sql = "CREATE TABLE test1 ( salary NUMBER ( 10 , 2 ) );"
    expected_result = "CREATE TABLE test1 ( salary NUMERIC(10,2) );"
    assert convert_data_types(oracle_sql) == expected_result

def test_varchar2_to_varchar():
    oracle_sql = "CREATE TABLE test2 ( name VARCHAR2 ( 100 ) );"
    expected_result = "CREATE TABLE test2 ( name VARCHAR(100) );"
    assert convert_data_types(oracle_sql) == expected_result

def test_unchanged_types():
    oracle_sql = "CREATE TABLE test3 ( mynumberfield INTEGER, salary NUMBERING_TYPE );"
    expected_result = "CREATE TABLE test3 ( mynumberfield INTEGER, salary NUMBERING_TYPE );"
    assert convert_data_types(oracle_sql) == expected_result

def test_raw_type_unchanged():
    oracle_sql = "CREATE TABLE test4 ( raw_column RAW );"
    expected_result = "CREATE TABLE test4 ( raw_column RAW );"
    assert convert_data_types(oracle_sql) == expected_result

def test_xmltype_unchanged():
    oracle_sql = "CREATE TABLE test5 ( content XMLTYPE );"
    expected_result = "CREATE TABLE test5 ( content XMLTYPE );"
    assert convert_data_types(oracle_sql) == expected_result

def test_multiple_columns_conversion():
    oracle_sql = "CREATE TABLE test6 ( id NUMBER(5); name VARCHAR2(50) );"
    expected_result = "CREATE TABLE test6 ( id NUMERIC(5); name VARCHAR(50) );"
    assert convert_data_types(oracle_sql) == expected_result

def test_mixed_case_types():
    oracle_sql = "CREATE TABLE test7 ( ID number(8, 3), NAME varchar2(30), Is_Active boolean );"
    expected_result = "CREATE TABLE test7 ( ID NUMERIC(8,3), NAME VARCHAR(30), Is_Active BOOLEAN );"
    assert convert_data_types(oracle_sql) == expected_result

def test_clob_to_text_conversion():
    oracle_sql = "CREATE TABLE test8 ( salary NUMBER(10,2), name VARCHAR2(100), info CLOB );"
    expected_result = "CREATE TABLE test8 ( salary NUMERIC(10,2), name VARCHAR(100), info TEXT );"
    assert convert_data_types(oracle_sql) == expected_result

def test_empty_table():
    oracle_sql = "CREATE TABLE empty_table ();"
    expected_result = "CREATE TABLE empty_table ();"
    assert convert_data_types(oracle_sql) == expected_result

def test_single_number_conversion():
    oracle_sql = "CREATE TABLE test10 ( salary NUMBER (12 , 2) );"
    expected_result = "CREATE TABLE test10 ( salary NUMERIC(12,2) );"
    assert convert_data_types(oracle_sql) == expected_result