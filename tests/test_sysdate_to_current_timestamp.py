import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.sysdate_to_current_timestamp import sysdate_to_current_timestamp

class TestOracleToPostgresDateConversion(unittest.TestCase):
    def test_simple_sysdate(self):
        oracle_sql = "SELECT SYSDATE FROM dual;"
        expected = "SELECT CURRENT_TIMESTAMP FROM dual;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_sysdate_with_alias(self):
        oracle_sql = "SELECT SYSDATE AS current_date FROM dual;"
        expected = "SELECT CURRENT_TIMESTAMP AS current_date FROM dual;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_sysdate_in_where_clause(self):
        oracle_sql = "SELECT * FROM orders WHERE created_date < SYSDATE - 1;"
        expected = "SELECT * FROM orders WHERE created_date < CURRENT_TIMESTAMP - 1;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_sysdate_in_update(self):
        oracle_sql = "UPDATE users SET last_login = SYSDATE WHERE id = 123;"
        expected = "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = 123;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_case_insensitive(self):
        oracle_sql = "select sysDate from dual;"
        expected = "select CURRENT_TIMESTAMP from dual;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_no_sysdate(self):
        oracle_sql = "SELECT CURRENT_TIMESTAMP FROM dual;"
        expected = "SELECT CURRENT_TIMESTAMP FROM dual;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_partial_matches_not_replaced(self):
        oracle_sql = "SELECT SYSDATE, MYSYDATETABLE FROM dual;"
        expected = "SELECT CURRENT_TIMESTAMP, MYSYDATETABLE FROM dual;"
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

    def test_complex_query(self):
        oracle_sql = """
            INSERT INTO audit_log (id, action_date, user_id)
            VALUES (audit_seq.NEXTVAL, SYSDATE, :user_id)
            RETURNING id INTO :new_id;
        """
        expected = """
            INSERT INTO audit_log (id, action_date, user_id)
            VALUES (audit_seq.NEXTVAL, CURRENT_TIMESTAMP, :user_id)
            RETURNING id INTO :new_id;
        """
        self.assertEqual(sysdate_to_current_timestamp(oracle_sql), expected)

if __name__ == '__main__':
    unittest.main()