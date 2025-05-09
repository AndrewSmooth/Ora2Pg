import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.regexp_like import regexp_like_to_postgres

class TestOracleRegexToPostgres(unittest.TestCase):
    def test_basic_regexp_like(self):
        oracle_sql = "SELECT * FROM users WHERE REGEXP_LIKE(name, '^A.*');"
        expected = "SELECT * FROM users WHERE name ~ '^A.*';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_case_insensitive_modifier(self):
        oracle_sql = "SELECT * FROM products WHERE REGEXP_LIKE(description, '^apple', 'i');"
        expected = "SELECT * FROM products WHERE description ~* '^apple';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_multiple_regexp_like(self):
        oracle_sql = """
            SELECT * FROM employees 
            WHERE REGEXP_LIKE(first_name, '^J') 
            AND REGEXP_LIKE(last_name, 'son$', 'i');
        """
        expected = """
            SELECT * FROM employees 
            WHERE first_name ~ '^J' 
            AND last_name ~* 'son$';
        """
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_with_whitespace_variations(self):
        oracle_sql = "SELECT * FROM logs WHERE REGEXP_LIKE( message,'error|fail' );"
        expected = "SELECT * FROM logs WHERE message ~ 'error|fail';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_complex_pattern(self):
        oracle_sql = "SELECT * FROM data WHERE REGEXP_LIKE(value, '^[A-Z]{2}\\d{4}$');"
        expected = "SELECT * FROM data WHERE value ~ '^[A-Z]{2}\\d{4}$';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_no_regexp_like(self):
        oracle_sql = "SELECT * FROM customers WHERE age > 30;"
        expected = "SELECT * FROM customers WHERE age > 30;"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_case_insensitive_function_name(self):
        oracle_sql = "SELECT * FROM books WHERE regexp_like(title, '^harry potter');"
        expected = "SELECT * FROM books WHERE title ~ '^harry potter';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_with_other_oracle_functions(self):
        oracle_sql = """
            SELECT id, SYSDATE 
            FROM orders 
            WHERE REGEXP_LIKE(order_number, '^ORD-\\d{5}')
            AND created_date > SYSDATE - 7;
        """
        expected = """
            SELECT id, SYSDATE 
            FROM orders 
            WHERE order_number ~ '^ORD-\\d{5}'
            AND created_date > SYSDATE - 7;
        """
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

    def test_empty_modifier(self):
        oracle_sql = "SELECT * FROM test WHERE REGEXP_LIKE(col, 'pattern', '');"
        expected = "SELECT * FROM test WHERE col ~ 'pattern';"
        self.assertEqual(regexp_like_to_postgres(oracle_sql), expected)

if __name__ == '__main__':
    unittest.main()