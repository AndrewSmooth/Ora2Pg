sql="SELECT * FROM clients WHERE INSTR(phone, '+7') > 0;"
#ожидаемый результат: SELECT * FROM clients WHERE POSITION('+7' IN phone) > 0;
#результат: SELECT * FROM clients WHERE POSITION('+7' IN phone) > 0;


sql="SELECT INSTR(name, 'a' FROM users;"
#ожидаемый результат: SELECT INSTR(name, 'a' FROM users;
#результат: SELECT INSTR(name, 'a' FROM users;

sql="SELECT INSTR(LOWER(name), 'a') FROM users;"
#ожидаемый результат: SELECT POSITION('a' IN LOWER(name)) FROM users;
#результат: SELECT POSITION('a' IN LOWER(name)) FROM users;

sql="SELECT INSTR(col1, 'x'), INSTR(col2, 'y') FROM table1;"
#ожидаемый результат: SELECT POSITION('x' IN col1), POSITION('y' IN col2) FROM table1;
#результат: SELECT POSITION('x' IN col1), POSITION('y' IN col2) FROM table1;

sql="SELECT * FROM users WHERE INSTR(email, '@') > 0;"
#ожидаемый результат: SELECT * FROM users WHERE POSITION('@' IN email) > 0;
#результат: SELECT * FROM users WHERE POSITION('@' IN email) > 0;

sql="SELECT INSTR('INSTR', 'INSTR') AS Position;"
#ожидаемый результат: SELECT POSITION('INSTR' IN 'INSTR') AS Position;
#результат: SELECT POSITION('INSTR' IN 'INSTR') AS Position;


sql="SELECT INSTR('abc123', 1) FROM dual;"
#ожидаемый результат: SELECT INSTR('abc123', 1) FROM dual;
#результат: SELECT POSITION(1 IN 'abc123') FROM dual;


sql="SELECT INSTR(SUBSTR(name, 1, 10), 'x') FROM employees;"
#ожидаемый результат: SELECT POSITION('x' IN SUBSTR(name, 1, 10)) FROM employees;
#результат: SELECT POSITION('x' IN SUBSTR(name, 1, 10)) FROM employees;

sql="SELECT INSTR(email, '@' FROM users;"
#ожидаемый результат: SELECT INSTR(email, '@' FROM users;
#результат: SELECT INSTR(email, '@' FROM users;

sql="SELECT * FROM (SELECT INSTR(email, '@') FROM users) sub;"
#ожидаемый результат: SELECT * FROM (SELECT POSITION('@' IN email) FROM users) sub;
#результат: SELECT * FROM (SELECT POSITION('@' IN email) FROM users) sub;

sql="SELECT INSTR(col1, 'x'), INSTR(col2, 'y'), INSTR(col3, 'z') FROM table1;"
#ожидаемый результат: SELECT POSITION('x' IN col1), POSITION('y' IN col2), POSITION('z' IN col3) FROM table1;
#результат: SELECT POSITION('x' IN col1), POSITION('y' IN col2), POSITION('z' IN col3) FROM table1;

