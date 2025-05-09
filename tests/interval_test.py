sql="SELECT to_DSINTERVAL('5') AS d FROM dual;"
#ожидаемый результат: SELECT INTERVAL '5 days' AS d FROM dual;
#результат: SELECT INTERVAL '5 days' AS d FROM dual;

sql="SELECT TO_dsinterval('5') AS d FROM dual;"
#ожидаемый результат: SELECT INTERVAL '5 days' AS d FROM dual;
#результат: SELECT INTERVAL '5 days' AS d FROM dual;


sql="SELECT TO_YMINTERVAL('0-0') FROM dual;"
#ожидаемый результат: SELECT INTERVAL '0 months' FROM dual;
#результат: SELECT INTERVAL '0 months' FROM dual;


sql="""SELECT
TO_DSINTERVAL('03:00:00') AS time,
TO_DSINTERVAL('7') AS days
TO_DSINTERVAL('0 00:00:00')
FROM dual;"""
#ожидаемый результат: SELECT
 #INTERVAL '0 days 03:00:00' AS time,
 #INTERVAL '7 days' AS days
 #INTERVAL '0 days 00:00:00'
 #FROM dual;
#результат: SELECT
        #INTERVAL '0 days 03:00:00' AS time,
        #INTERVAL '7 days' AS days
        #INTERVAL '0 days 00:00:00'
    #FROM dual;


sql="SELECT TO_YMINTERVAL('02-06') FROM dual;"
#ожидаемый результат: SELECT INTERVAL '2 years 6 months' FROM dual;
#результат: SELECT INTERVAL '2 years 6 months' FROM dual;

sql="SELECT TO_DSINTERVAL(' 10 04:00:00 ')"
#ожидаемый результат: SELECT INTERVAL '10 days 04:00:00'
#результат: SELECT INTERVAL '10 days 04:00:00'


sql="SELECT TO_DSINTERVAL('0 00:00:00') FROM dual;"
#ожидаемый результат: SELECT INTERVAL '0 days 00:00:00' FROM dual;
#результат: SELECT INTERVAL '0 days 00:00:00' FROM dual;


sql="SELECT TO_DSINTERVAL('5 12:30:45') FROM dual;"
#ожидаемый результат: SELECT INTERVAL '5 days 12:30:45' FROM dual;
#результат: SELECT INTERVAL '5 days 12:30:45' FROM dual;


sql="SELECT TO_YMINTERVAL('1-2') AS ym FROM dual;"
#ожидаемый результат: SELECT INTERVAL '1 years 2 months' AS ym FROM dual;
#результат: SELECT INTERVAL '1 years 2 months' AS ym FROM dual;


sql="SELECT TO_DSINTERVAL('4 02:00:00') AS full FROM dual;"
#ожидаемый результат: SELECT INTERVAL '4 days 02:00:00' AS full FROM dual;
#результат: SELECT INTERVAL '4 days 02:00:00' AS full FROM dual;
