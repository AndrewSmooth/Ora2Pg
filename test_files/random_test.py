import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dbmsrandom import dbms_random_to_random

class TestDbmsRandomToRandom(unittest.TestCase):
    def test_1(self):
        sql = "SELECT DBMS_RANDOM.VALUE() FROM dual"
        expected = "SELECT RANDOM() FROM dual"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_2(self):
        sql = "SELECT DBMS_RANDOM.VALUE(1, 10) FROM dual"
        expected = "SELECT (1 + ((10 - 1) * RANDOM())) FROM dual"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_3(self):
        sql = "SELECT DBMS_RANDOM.NORMAL() FROM dual"
        expected = "SELECT RANDOM() FROM dual"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_4(self):
        sql = "INSERT INTO table VALUES (DBMS_RANDOM.VALUE())"
        expected = "INSERT INTO table VALUES (RANDOM())"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_5(self):
        sql = "UPDATE table SET col = DBMS_RANDOM.VALUE(0.1, 0.9) WHERE id = 1"
        expected = "UPDATE table SET col = (0.1 + ((0.9 - 0.1) * RANDOM())) WHERE id = 1"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_6(self):
        sql = "SELECT dbms_random.value() FROM dual"
        expected = "SELECT RANDOM() FROM dual"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_7(self):
        sql = "UPDATE table SET col = DBMS_RANDOM.VALUE(0.1, 0.8) WHERE id = 1"
        expected = "UPDATE table SET col = (0.1 + ((0.8 - 0.1) * RANDOM())) WHERE id = 1"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_8(self):
        sql = "CREATE FUNCTION fn() RETURNS NUMBER AS BEGIN RETURN DBMS_RANDOM.VALUE(); END;"
        expected = "CREATE FUNCTION fn() RETURNS NUMBER AS BEGIN RETURN RANDOM(); END;"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_9(self):
        sql = "SELECT DBMS_RANDOM.VALUE(a, b) FROM table"
        expected = "SELECT (a + ((b - a) * RANDOM())) FROM table"
        self.assertEqual(dbms_random_to_random(sql), expected)

    def test_10(self):
        sql = "SELECT DBMS_RANDOM.NORMAL() * 100 FROM stats"
        expected = "SELECT RANDOM() * 100 FROM stats"
        self.assertEqual(dbms_random_to_random(sql), expected)

if __name__ == '__main__':
    unittest.main()
