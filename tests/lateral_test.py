import pytest
from lateral import oracle_unpivot_to_postgresql

def test_simple_unpivot():
    oracle_sql = """SELECT id, name, value
FROM products
UNPIVOT (value FOR name IN (price, weight, quantity))"""
    expected_result = """SELECT id, name, value
FROM products
JOIN LATERAL (VALUES
        ('price', price),
        ('weight', weight),
        ('quantity', quantity)
    ) AS unpivoted(name, value) ON true"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result

def test_unpivot_with_aliases():
    oracle_sql = """SELECT emp_id, metric_type, metric_value
FROM employee_stats
UNPIVOT (
    metric_value FOR metric_type IN (
        sales AS 'TOTAL_SALES', 
        hours AS 'WORK_HOURS'
    )
)"""
    expected_result = """SELECT emp_id, metric_type, metric_value
FROM employee_stats
JOIN LATERAL (VALUES
        ('TOTAL_SALES', sales),
        ('WORK_HOURS', hours)
    ) AS unpivoted(metric_type, metric_value) ON true"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result

def test_unpivot_with_where_clause():
    oracle_sql = """SELECT id, k, v
FROM data
UNPIVOT (
    v FOR k IN (
        col1 AS 'c1',
        col2 AS 'c2',
        col3 AS 'c3'
    )
) WHERE id > 100"""
    expected_result = """SELECT id, k, v
FROM data
JOIN LATERAL (VALUES
        ('c1', col1),
        ('c2', col2),
        ('c3', col3)
    ) AS unpivoted(k, v) ON true WHERE id > 100"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result

def test_already_converted_query():
    oracle_sql = """SELECT a, b FROM t
JOIN LATERAL (VALUES
        ('x', x),
        ('y', y),
        ('z', z)
    ) AS unpivoted(a, b) ON true"""
    expected_result = """SELECT a, b FROM t
JOIN LATERAL (VALUES
        ('x', x),
        ('y', y),
        ('z', z)
    ) AS unpivoted(a, b) ON true"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result

def test_mixed_column_aliases():
    oracle_sql = """SELECT * FROM dataset
UNPIVOT (
    val FOR col IN (
        "col1" AS 'Column1', 
        col2, 
        col3 AS 'Third_Column'
    )
)"""
    expected_result = """SELECT * FROM dataset
JOIN LATERAL (VALUES
        ('Column1', col1),
        ('col2', col2),
        ('Third_Column', col3)
    ) AS unpivoted(col, val) ON true"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result

def test_multiline_formatting():
    oracle_sql = """SELECT id, name, value
    FROM products
    UNPIVOT (value FOR name IN (price, weight, quantity))"""
    expected_result = """SELECT id, name, value
    FROM products
    JOIN LATERAL (VALUES
        ('price', price),
        ('weight', weight),
        ('quantity', quantity)
    ) AS unpivoted(name, value) ON true"""
    assert oracle_unpivot_to_postgresql(oracle_sql) == expected_result