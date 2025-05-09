
sql_query="CREATE TABLE test1 ( salary NUMBER ( 10 , 2 ) );"
#ожидаемый результат:CREATE TABLE test1 ( salary NUMERIC(10,2) );
#Результат:CREATE TABLE test1 ( salary NUMERIC(10,2) );

sql_query="CREATE TABLE test2 ( name VARCHAR2 ( 100 ) );"
#ожидаемый результат:CREATE TABLE test2 ( name VARCHAR(100) );
#Результат:CREATE TABLE test2 ( name VARCHAR ( 100 ) );

sql_query="CREATE TABLE test3 ( mynumberfield INTEGER, salary NUMBERING_TYPE );"
#ожидаемый результат:CREATE TABLE test3 ( mynumberfield INTEGER, salary NUMBERING_TYPE );
#Результат:CREATE TABLE test3 ( mynumberfield INTEGER, salary NUMBERING_TYPE );

sql_query="CREATE TABLE test4 ( raw_column RAW );"
#ожидаемый результат:CREATE TABLE test4 ( raw_column RAW );
#Результат:CREATE TABLE test4 ( raw_column RAW );


sql_query="CREATE TABLE test5 ( content XMLTYPE );"
#ожидаемый результат:CREATE TABLE test5 ( content XMLTYPE );
#Результат:CREATE TABLE test5 ( content XMLTYPE );


sql_query="CREATE TABLE test6 ( id NUMBER(5); name VARCHAR2(50) );"
#ожидаемый результат:CREATE TABLE test6 ( id NUMERIC(5); name VARCHAR(50) );
#Результат:CREATE TABLE test6 ( id NUMERIC(5); name VARCHAR(50) );



sql_query="CREATE TABLE test7 ( ID number(8, 3), NAME varchar2(30), Is_Active boolean );"
#ожидаемый результат:CREATE TABLE test7 ( ID NUMERIC(8,3), NAME VARCHAR(30), Is_Active BOOLEAN );
#Результат:CREATE TABLE test7 ( ID NUMERIC(8,3), NAME VARCHAR(30), Is_Active BOOLEAN );

sql_query="CREATE TABLE test8 ( salary NUMBER(10,2), name VARCHAR2(100), info CLOB );"
#ожидаемый результат:CREATE TABLE test8 ( salary NUMERIC(10,2), name VARCHAR(100), info TEXT );
#Результат:CREATE TABLE test8 ( salary NUMERIC(10,2), name VARCHAR(100), info TEXT );



sql_query="CREATE TABLE empty_table ();"
#ожидаемый результат:CREATE TABLE empty_table ();
#Результат:CREATE TABLE empty_table ();


sql_query="CREATE TABLE test10 ( salary NUMBER (12 , 2) );"
#ожидаемый результат:CREATE TABLE test10 ( salary NUMERIC(12,2) );
#Результат:CREATE TABLE test10 ( salary NUMERIC(12,2) );
