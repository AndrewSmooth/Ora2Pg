import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LISTAGG import listagg_to_string_agg

class TestListAggToStringAgg(unittest.TestCase):
    def test_1(self):
        sql = "SELECT LISTAGG(name, ',') WITHIN GROUP (ORDER BY id) FROM users"
        expected = "SELECT STRING_AGG(name, ',' ORDER BY id) FROM users"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_2(self):
        sql = "SELECT department, LISTAGG(employee, '; ') WITHIN GROUP (ORDER BY hire_date) FROM staff GROUP BY department"
        expected = "SELECT department, STRING_AGG(employee, '; ' ORDER BY hire_date) FROM staff GROUP BY department"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_3(self):
        sql = "SELECT LISTAGG(product, ', ' ORDER BY price DESC) FROM products"
        expected = "SELECT STRING_AGG(product, ', ' ORDER BY price DESC) FROM products"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_4(self):
        sql = "SELECT id, LISTAGG(DISTINCT tag, '#') WITHIN GROUP (ORDER BY tag) FROM items"
        expected = "SELECT id, STRING_AGG(DISTINCT tag, '#' ORDER BY tag) FROM items"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_5(self):
        sql = "SELECT LISTAGG(name, '|' ORDER BY name ASC) FILTER (WHERE active = TRUE) FROM customers"
        expected = "SELECT STRING_AGG(name, '|' ORDER BY name ASC) FILTER (WHERE active = TRUE) FROM customers"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_6(self):
        sql = "SELECT category, LISTAGG(name, ', ') WITHIN GROUP (ORDER BY name) AS products FROM goods GROUP BY category"
        expected = "SELECT category, STRING_AGG(name, ', ' ORDER BY name) AS products FROM goods GROUP BY category"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_7(self):
        sql = "SELECT LISTAGG(SUBSTR(name, 1, 10), ',') WITHIN GROUP (ORDER BY id) FROM users"
        expected = "SELECT STRING_AGG(SUBSTR(name, 1, 10), ',' ORDER BY id) FROM users"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_8(self):
        sql = "SELECT LISTAGG(NVL(description, 'N/A'), ';') WITHIN GROUP (ORDER BY id) FROM products"
        expected = "SELECT STRING_AGG(NVL(description, 'N/A'), ';' ORDER BY id) FROM products"
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_9(self):
        sql = """SELECT department,
                      LISTAGG(employee_id || ':' || last_name, '|') 
                      WITHIN GROUP (ORDER BY hire_date)
               FROM employees
               GROUP BY department"""
        expected = """SELECT department,
                      STRING_AGG(employee_id || ':' || last_name, '|' ORDER BY hire_date)
               FROM employees
               GROUP BY department"""
        self.assertEqual(listagg_to_string_agg(sql), expected)

    def test_10(self):
        sql = "SELECT department_id, LISTAGG(employee_name, ', ' ORDER BY salary DESC) FROM emp GROUP BY department_id HAVING COUNT(*) > 5"
        expected = "SELECT department_id, STRING_AGG(employee_name, ', ' ORDER BY salary DESC) FROM emp GROUP BY department_id HAVING COUNT(*) > 5"
        self.assertEqual(listagg_to_string_agg(sql), expected)

if __name__ == '__main__':
    unittest.main()