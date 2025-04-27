import unittest
import minus


class TestOracleToPostgresConversion(unittest.TestCase):
    def test_simple_minus(self):
        sql = "SELECT * FROM a MINUS SELECT * FROM b"
        expected = "SELECT * FROM a EXCEPT SELECT * FROM b"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), expected)

    def test_case_insensitivity(self):
        sql = "SELECT * FROM a minus SELECT * FROM b"
        expected = "SELECT * FROM a EXCEPT SELECT * FROM b"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), expected)

    def test_inside_single_quotes(self):
        sql = "SELECT 'MINUS' AS operator FROM table"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), sql)

    def test_inside_double_quotes(self):
        sql = 'SELECT "MINUS" AS operator FROM table'
        self.assertEqual(minus.convert_oracle_to_postgres(sql), sql)

    def test_in_comment(self):
        sql = "SELECT * FROM table -- MINUS operation here"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), sql)

    def test_combined_case(self):
        sql = """SELECT MINUS FROM test -- MINUS
                 WHERE col = 'MINUS' OR name = "MINUS" MINUS"""
        expected = """SELECT EXCEPT FROM test -- MINUS
                 WHERE col = 'MINUS' OR name = "MINUS" EXCEPT"""
        self.assertEqual(minus.convert_oracle_to_postgres(sql), expected)

    def test_escaped_quotes(self):
        sql = "SELECT 'Don\\'t MINUS' FROM table MINUS"
        expected = "SELECT 'Don\\'t MINUS' FROM table EXCEPT"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), expected)

    def test_multiline_query(self):
        sql = """SELECT *
                 FROM table1
                 MINUS
                 SELECT *
                 FROM table2
                 WHERE value = 'MINUS'"""
        expected = """SELECT *
                 FROM table1
                 EXCEPT
                 SELECT *
                 FROM table2
                 WHERE value = 'MINUS'"""
        self.assertEqual(minus.convert_oracle_to_postgres(sql), expected)

    def test_part_of_larger_word(self):
        sql = "SELECT MINUSION FROM table"
        self.assertEqual(minus.convert_oracle_to_postgres(sql), sql)


if __name__ == '__main__':
    unittest.main()
