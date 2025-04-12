sql="SELECT BIN_TO_NUM('1, 0, 1') FROM dual;"
#ожидаемый результат: SELECT ('1, 0, 1'::bit(1))::integer FROM dual
#результат: SELECT ('1'::bit(1))::integer FROM dual

sql="SELECT BIN_TO_NUM('1, 0, A') FROM dual;"
#ожидаемый результат: SELECT ('1' || '0' || 'A')::bit(3)::integer FROM dual;
#результат SELECT ('1 || 0 || A')::bit(3)::integer FROM dual;

sql="SELECT BIN_TO_NUM(' 1 , 0 , 1 ') FROM dual;"
#ожидаемый результат: SELECT ('101'::bit(3))::integer FROM dual;
#результат SELECT ('101'::bit(3))::integer FROM dual;

sql="SELECT BIN_TO_NUM('1, 0, 1, 1, 0, 1, 1, 1') FROM dual;"
#ожидаемый результат: SELECT ('10110111'::bit(8))::integer FROM dual;
#результат SELECT ('10110111'::bit(8))::integer FROM dual;

sql="SELECT BIN_TO_NUM('') FROM dual;"
#ожидаемый результат: SELECT (''::bit(1))::integer FROM dual;
#результат SELECT ('')::bit(1)::integer FROM dual;

sql="SELECT BIN_TO_NUM('1, 0') || BIN_TO_NUM('1, 1') FROM dual;"
#ожидаемый результат: SELECT ('10'::bit(2))::integer || ('11'::bit(2))::integer FROM dual;
#результат SELECT ('10'::bit(2))::integer|| ('11'::bit(2))::integer FROM dual;

sql="SELECT BIN_TO_NUM( 1 , 0\t,\t1 ) AS res FROM dual"
#ожидаемый результат: SELECT ('101'::bit(3))::integer AS res FROM dual
#результат SELECT ('101'::bit(3))::integer AS res FROM dual


sql="SELECT BIN_TO_NUM(col1 + 1, col2) FROM t"
#ожидаемый результат: SELECT (col1 + 1 || col2)::bit(2)::integer FROM t
#результат SELECT (col1 + 1 || col2)::bit(2)::integer FROM t

sql="SELECT * FROM t WHERE BIN_TO_NUM(f1, f2) > 2"
#ожидаемый результат: SELECT * FROM t WHERE (f1 || f2)::bit(2)::integer > 2
#результат SELECT * FROM t WHERE (f1 || f2)::bit(2)::integer > 2


sql="SELECT BITAND(BIN_TO_NUM(a, b, c), 3) AS masked FROM t"
#ожидаемый результат: SELECT BITAND((a || b || c)::bit(3)::integer, 3) AS masked FROM t
#результат SELECT BITAND((a || b || c)::bit(3)::integer, 3) AS masked FROM t



sql="SELECT BIN_TO_NUM(flag1 AND flag2, flag3) FROM t"
#ожидаемый результат: SELECT (flag1 AND flag2 || flag3)::bit(2)::integer FROM t
#результат SELECT (flag1 AND flag2 || flag3)::bit(2)::integer FROM t


