import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from from_dual import convert_from_dual

def test_remove_from_dual_simple():
    query = "SELECT 1 FROM DUAL;"
    expected = "SELECT 1"
    assert convert_from_dual(query) == expected

def test_remove_from_dual_with_where():
    query = "SELECT * FROM DUAL WHERE 1=1"
    expected = "SELECT * WHERE 1=1"
    assert convert_from_dual(query) == expected

def test_remove_from_dual_with_group_by():
    query = "SELECT SUM(x) FROM DUAL GROUP BY y"
    expected = "SELECT SUM(x) GROUP BY y"
    assert convert_from_dual(query) == expected

def test_parentheses_around_select():
    query = "( SELECT 1 FROM DUAL )"
    expected = "SELECT 1 FROM DUAL"
    assert convert_from_dual(query) == expected
def test_no_dual_present():
    query = "SELECT * FROM my_table"
    expected = "SELECT * FROM my_table"
    assert convert_from_dual(query) == expected

def test_dual_case_insensitive():
    query = "select 1 from dual;"
    expected = "select 1"
    assert convert_from_dual(query) == expected