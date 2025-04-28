import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sdgs import merge_to_delete_update_insert 

def merge_to_delete_update_insrt():
    oracle_sql = """
    MERGE INTO employees e
    USING new_employees ne
    ON (e.id = ne.id)
    WHEN MATCHED THEN
        UPDATE SET e.name = ne.name
    WHEN NOT MATCHED THEN
        INSERT (id, name) VALUES (ne.id, ne.name);
    """
    result = merge_to_delete_update_insert(oracle_sql, use_update=True)
    assert "UPDATE employees AS e" in result
    assert "INSERT INTO employees" in result

def test_merge_with_delete():
    oracle_sql = """
    MERGE INTO employees e
    USING former_employees fe
    ON (e.id = fe.id)
    WHEN MATCHED THEN
        DELETE WHERE e.status = 'inactive';
    """
    result = merge_to_delete_update_insert(oracle_sql, use_update=False)
    assert "DELETE FROM employees AS e" in result
    assert "WHERE EXISTS" in result

def test_merge_with_insert_only():
    oracle_sql = """
    MERGE INTO employees e
    USING candidates c
    ON (e.id = c.id)
    WHEN NOT MATCHED THEN
        INSERT (id, name) VALUES (c.id, c.name);
    """
    result = merge_to_delete_update_insert(oracle_sql, use_update=True)
    assert "INSERT INTO employees" in result
    assert "SELECT c.id, c.name" in result