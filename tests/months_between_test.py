import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.months_between import months_between

class TestMonthsBetween(unittest.TestCase):
    def test_1(self):
        sql = "SELECT MONTHS_BETWEEN(date1, date2) FROM table"
        expected = "SELECT ((EXTRACT(YEAR FROM AGE(date1, date2)) * 12) + EXTRACT(MONTH FROM AGE(date1, date2))) FROM table"
        self.assertEqual(months_between(sql), expected)

    def test_2(self):
        sql = "SELECT * FROM table WHERE MONTHS_BETWEEN(date1, date2) > 12"
        expected = "SELECT * FROM table WHERE ((EXTRACT(YEAR FROM AGE(date1, date2)) * 12) + EXTRACT(MONTH FROM AGE(date1, date2))) > 12"
        self.assertEqual(months_between(sql), expected)

    def test_3(self):
        sql = "SELECT id, MONTHS_BETWEEN(end_date, start_date) FROM contracts"
        expected = "SELECT id, ((EXTRACT(YEAR FROM AGE(end_date, start_date)) * 12) + EXTRACT(MONTH FROM AGE(end_date, start_date))) FROM contracts"
        self.assertEqual(months_between(sql), expected)

    def test_4(self):
        sql = "UPDATE table SET col = MONTHS_BETWEEN(date1, date2)"
        expected = "UPDATE table SET col = ((EXTRACT(YEAR FROM AGE(date1, date2)) * 12) + EXTRACT(MONTH FROM AGE(date1, date2)))"
        self.assertEqual(months_between(sql), expected)

    def test_5(self):
        sql = "SELECT AVG(MONTHS_BETWEEN(end_date, start_date)) FROM projects"
        expected = "SELECT AVG(((EXTRACT(YEAR FROM AGE(end_date, start_date)) * 12) + EXTRACT(MONTH FROM AGE(end_date, start_date)))) FROM projects"
        self.assertEqual(months_between(sql), expected)

    def test_6(self):
        sql = "SELECT * FROM table WHERE MONTHS_BETWEEN(CURRENT_DATE, created_at) < 6"
        expected = "SELECT * FROM table WHERE ((EXTRACT(YEAR FROM AGE(CURRENT_DATE, created_at)) * 12) + EXTRACT(MONTH FROM AGE(CURRENT_DATE, created_at))) < 6"
        self.assertEqual(months_between(sql), expected)

    def test_7(self):
        sql = "SELECT MONTHS_BETWEEN(date1+INTERVAL '1 day', date2) FROM events"
        expected = "SELECT ((EXTRACT(YEAR FROM AGE(date1+INTERVAL '1 day', date2)) * 12) + EXTRACT(MONTH FROM AGE(date1+INTERVAL '1 day', date2))) FROM events"
        self.assertEqual(months_between(sql), expected)

    def test_8(self):
        sql = "SELECT MONTHS_BETWEEN(MAX(date), MIN(date)) FROM table"
        expected = "SELECT ((EXTRACT(YEAR FROM AGE(MAX(date), MIN(date)) * 12) + EXTRACT(MONTH FROM AGE(MAX(date), MIN(date)))) FROM table"
        self.assertEqual(months_between(sql), expected)
    def test_9(self):
        sql = "SELECT product_id, MONTHS_BETWEEN(discontinued_date, release_date) AS months_available FROM products HAVING MONTHS_BETWEEN(discontinued_date, release_date) > 24"
        expected = "SELECT product_id, ((EXTRACT(YEAR FROM AGE(discontinued_date, release_date)) * 12) + EXTRACT(MONTH FROM AGE(discontinued_date, release_date))) AS months_available FROM products HAVING ((EXTRACT(YEAR FROM AGE(discontinued_date, release_date)) * 12) + EXTRACT(MONTH FROM AGE(discontinued_date, release_date))) > 24"
        self.assertEqual(months_between(sql), expected)

    def test_10(self):
        sql = """SELECT customer_id, 
                MONTHS_BETWEEN(last_purchase_date, first_purchase_date) AS loyalty_months
                FROM customers
                WHERE MONTHS_BETWEEN(CURRENT_DATE, last_purchase_date) < 3"""
        expected = """SELECT customer_id, 
                ((EXTRACT(YEAR FROM AGE(last_purchase_date, first_purchase_date)) * 12) + EXTRACT(MONTH FROM AGE(last_purchase_date, first_purchase_date))) AS loyalty_months
                FROM customers
                WHERE ((EXTRACT(YEAR FROM AGE(CURRENT_DATE, last_purchase_date)) * 12) + EXTRACT(MONTH FROM AGE(CURRENT_DATE, last_purchase_date))) < 3"""
        self.assertEqual(months_between(sql), expected)

if __name__ == '__main__':
    unittest.main()
