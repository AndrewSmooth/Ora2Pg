sql="SELECT TO_NUMBER(col1) FROM table1;"
#ожидаемый результат: SELECT CAST(col1 AS NUMERIC) FROM table1;
#результат: SELECT CAST(col1 AS NUMERIC) FROM table1;

sql="SELECT TO_NUMBER( col2 ) FROM table2;"
#Ожидаемый результат: SELECT CAST(col2 AS NUMERIC) FROM table2;
#Результат: SELECT CAST(col2 AS NUMERIC) FROM table2;

sql="SELECT TO_NUMBER('111') FROM test"
#ожидаемый результат: SELECT CAST('111' AS NUMERIC) FROM test
#результат: SELECT CAST('111' AS NUMERIC) FROM test


sql="SELECT TO_NUMBER('123' FROM dual;"
#ожидаемый результат: SELECT TO_NUMBER('123' FROM dual;
#результат: SELECT TO_NUMBER('123' FROM dual;

sql="SELECT id FROM (SELECT TO_NUMBER(salary) FROM employees) sub;"
#ожидаемый результат: SELECT id FROM (SELECT CAST(salary AS NUMERIC) FROM employees) sub;
#результат: SELECT id FROM (SELECT CAST(salary AS NUMERIC) FROM employees) sub;


sql="SELECT TO_NUMBER(col1 + col2) FROM table5;"
#ожидаемый результат: SELECT CAST(col1 + col2 AS NUMERIC) FROM table5;
#результат: SELECT CAST(col1 + col2 AS NUMERIC) FROM table5;

sql="SELECT to_number('123'), To_Number(col), TO_number(col) FROM dual;"
#ожидаемый результат: SELECT CAST('123' AS NUMERIC), CAST(col AS NUMERIC), CAST(col AS NUMERIC) FROM dual;
#результат: SELECT CAST('123' AS NUMERIC), CAST(col AS NUMERIC), CAST(col AS NUMERIC) FROM dual;

sql="SELECT 'Call TO_NUMBER here' AS message;"
#ожидаемый результат: SELECT 'Call TO_NUMBER here' AS message;
#результат: SELECT 'Call TO_NUMBER here' AS message;

sql="SELECT TO_NUMBER(col1), TO_NUMBER('789') FROM table3;"
#ожидаемый результат: SELECT CAST(col1 AS NUMERIC), CAST('789' AS NUMERIC) FROM table3;
#результат: SELECT CAST(col1 AS NUMERIC), CAST('789' AS NUMERIC) FROM table3;

sql="SELECT TO_NUMBER(SUBSTR(col, 1, 3)) FROM table4;"
#ожидаемый результат: SELECT CAST(SUBSTR(col, 1, 3) AS NUMERIC) FROM table4;
#результат: SELECT CAST(SUBSTR(col, 1, 3 AS NUMERIC)) FROM table4;
