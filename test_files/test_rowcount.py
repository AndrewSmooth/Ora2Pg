import pytest
from rowcount import rowcount


def test_simple_update():
    oracle_sql = """
    BEGIN
        UPDATE employees SET salary = salary * 1.1 WHERE department_id = 10;
        IF SQL%ROWCOUNT > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Rows updated: ' || SQL%ROWCOUNT);
        END IF;
    END;
    """
    
    expected_postgres = """
    BEGIN
        UPDATE employees SET salary = salary * 1.1 WHERE department_id = 10;
  GET DIAGNOSTICS row_count = ROW_COUNT;
        IF row_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Rows updated: ' || row_count);
        END IF;
    END;
    """
    
    assert rowcount(oracle_sql) == expected_postgres

def test_complex_merge_operation():
    oracle_sql = """
    BEGIN
        MERGE INTO target t
        USING source s ON (t.id = s.id)
        WHEN MATCHED THEN UPDATE SET t.value = s.value
        WHEN NOT MATCHED THEN INSERT (id, value) VALUES (s.id, s.value);
        processed_count := SQL%ROWCOUNT;
    END;
    """
    
    expected_postgres = """
    BEGIN
        MERGE INTO target t
        USING source s ON (t.id = s.id)
        WHEN MATCHED THEN UPDATE SET t.value = s.value
        WHEN NOT MATCHED THEN INSERT (id, value) VALUES (s.id, s.value);
  GET DIAGNOSTICS row_count = ROW_COUNT;
        processed_count := row_count;
    END;
    """
    
    assert rowcount(oracle_sql) == expected_postgres

def test_multiple_occurrences_in_one_block():
    oracle_sql = """
    BEGIN
        UPDATE products SET price = price * 1.05 WHERE category = 'A';
        IF SQL%ROWCOUNT > 0 THEN
            DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT || ' products updated');
        END IF;
        
        -- Еще одно использование
        updated_count := SQL%ROWCOUNT;
    END;
    """
    
    expected_postgres = """
    BEGIN
        UPDATE products SET price = price * 1.05 WHERE category = 'A';
  GET DIAGNOSTICS row_count = ROW_COUNT;
        IF row_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE(row_count || ' products updated');
        END IF;
        
        -- Еще одно использование
        updated_count := row_count;
    END;
    """
    
    assert rowcount(oracle_sql) == expected_postgres

def test_empty_input():
    assert rowcount("") == ""