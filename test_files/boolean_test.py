import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from number_to_bool import number1_to_boolean


class TestNumber1ToBoolean(unittest.TestCase):
    def test_1(self):
        sql = "CREATE TABLE users (id NUMBER, active NUMBER(1))"
        expected = "CREATE TABLE users (id NUMBER, active BOOLEAN)"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_2(self):
        sql = "ALTER TABLE products ADD COLUMN available NUMBER(1)"
        expected = "ALTER TABLE products ADD COLUMN available BOOLEAN"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_3(self):
        sql = "SELECT * FROM table WHERE flag = NUMBER(1)"
        expected = "SELECT * FROM table WHERE flag = BOOLEAN"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_4(self):
        sql = "NUMBER(1) NUMBER(10) NUMBER(1,0)"
        expected = "BOOLEAN NUMBER(10) NUMBER(1,0)"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_5(self):
        sql = "CREATE TABLE test (col1 NUMBER(1), col2 NUMBER(1))"
        expected = "CREATE TABLE test (col1 BOOLEAN, col2 BOOLEAN)"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_6(self):
        sql = "COMMENT ON COLUMN table.column IS 'NUMBER(1) field'"
        expected = "COMMENT ON COLUMN table.column IS 'BOOLEAN field'"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_7(self):
        sql = "NUMBER( 1 )"
        expected = "BOOLEAN"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_8(self):
        sql = "number(1)"
        expected = "BOOLEAN"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_9(self):
        sql = "CREATE TABLE types (a NUMBER(1), b NUMBER(2), c NUMBER(1,1))"
        expected = "CREATE TABLE types (a BOOLEAN, b NUMBER(2), c NUMBER(1,1))"
        self.assertEqual(number1_to_boolean(sql), expected)

    def test_10(self):
        sql = "SELECT CAST(1 AS NUMBER(1)) FROM dual"
        expected = "SELECT CAST(1 AS BOOLEAN) FROM dual"
        self.assertEqual(number1_to_boolean(sql), expected)

if __name__ == '__main__':
    unittest.main()