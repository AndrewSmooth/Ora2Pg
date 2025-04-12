import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from NVL_TO_COALESCE import nvl_to_coalesce
class TestNvlToCoalesce(unittest.TestCase):
        def test_1(self):
            oracle_sql = "SELECT NVL(column1, 'default') FROM table1"
            expected = "SELECT COALESCE(column1, 'default') FROM table1"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_2(self):
            oracle_sql = "SELECT NVL(salary * bonus, 0) FROM employees"
            expected = "SELECT COALESCE(salary * bonus, 0) FROM employees"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_3(self):
            oracle_sql = """
            SELECT 
                order_id,
                NVL(customer_name, 'Anonymous') AS customer,
                NVL(discount_amount, 0) AS discount
            FROM orders
            WHERE NVL(is_canceled, FALSE) = FALSE
            """
            expected = """
            SELECT 
                order_id,
                COALESCE(customer_name, 'Anonymous') AS customer,
                COALESCE(discount_amount, 0) AS discount
            FROM orders
            WHERE COALESCE(is_canceled, FALSE) = FALSE
            """
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_4(self):
            oracle_sql = "SELECT NVL(col1, 0), NVL(col2, 'N/A') FROM table"
            expected = "SELECT COALESCE(col1, 0), COALESCE(col2, 'N/A') FROM table"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_5(self):
            oracle_sql = "SELECT NVL(SUBSTR(name, 1, 10), 'Unknown') FROM users"
            expected = "SELECT COALESCE(SUBSTR(name, 1, 10), 'Unknown') FROM users"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_6(self):
            oracle_sql = """SELECT id, NVL(description, 'No description'), 
                        NVL(price * quantity, 0) FROM products WHERE NVL(stock, 0) > 0"""
            expected = """SELECT id, COALESCE(description, 'No description'), 
                        COALESCE(price * quantity, 0) FROM products WHERE COALESCE(stock, 0) > 0"""
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        
        def test_7(self):
                oracle_sql = "SELECT NVL(column1, NULL) FROM table1"
                expected = "SELECT COALESCE(column1, NULL) FROM table1"
                self.assertEqual(nvl_to_coalesce(oracle_sql), expected)

        def test_8(self):
            oracle_sql = "SELECT NVL(column1, CURRENT_TIMESTAMP) FROM table1"
            expected = "SELECT COALESCE(column1, CURRENT_TIMESTAMP) FROM table1"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)

        def test_9(self):
            oracle_sql = "SELECT NVL(CASE WHEN x > 0 THEN 1 ELSE 0 END, -1) FROM table1"
            expected = "SELECT COALESCE(CASE WHEN x > 0 THEN 1 ELSE 0 END, -1) FROM table1"
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
        def test_14(self):
            oracle_sql = """
            SELECT 
                employee_id,
                NVL(commission_pct, 0) * salary AS total_compensation,
                NVL(department_id, 99) AS department
            FROM 
                employees
            WHERE 
                NVL(termination_date, DATE '9999-12-31') > CURRENT_DATE
            """
            expected = """
            SELECT 
                employee_id,
                COALESCE(commission_pct, 0) * salary AS total_compensation,
                COALESCE(department_id, 99) AS department
            FROM 
                employees
            WHERE 
                COALESCE(termination_date, DATE '9999-12-31') > CURRENT_DATE
            """
            self.assertEqual(nvl_to_coalesce(oracle_sql), expected)
            
if __name__ == '__main__':
    unittest.main()