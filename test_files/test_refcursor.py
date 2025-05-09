import pytest
from refcursor import refcursor 

# Тестовые случаи
TEST_CASES = [
    # 1. Простая функция с возвратом курсора
    (
        """
        CREATE OR REPLACE FUNCTION get_emps RETURN SYS_REFCURSOR IS
          cur SYS_REFCURSOR;
        BEGIN
          OPEN cur FOR SELECT * FROM emp;
          RETURN cur;
        END;
        """,
        """
        CREATE OR REPLACE FUNCTION get_emps RETURNS REFCURSOR IS
          cur REFCURSOR;
        BEGIN
          OPEN cur FOR SELECT * FROM emp;
          RETURN cur;
        END;
        """
    ),
    # 2. Функция с параметром и курсором
    (
        """
        CREATE FUNCTION get_dept_emps(dept_id NUMBER) RETURN SYS_REFCURSOR IS
          rc SYS_REFCURSOR;
        BEGIN
          OPEN rc FOR SELECT * FROM emp WHERE deptno = dept_id;
          RETURN rc;
        END;
        """,
        """
        CREATE FUNCTION get_dept_emps(dept_id NUMBER) RETURNS REFCURSOR IS
          rc REFCURSOR;
        BEGIN
          OPEN rc FOR SELECT * FROM emp WHERE deptno = dept_id;
          RETURN rc;
        END;
        """
    ),
    # 3. Блок с обработкой курсора
    (
        """
        DECLARE
          emp_cur SYS_REFCURSOR;
          emp_rec emp%ROWTYPE;
        BEGIN
          emp_cur := get_emps();
          LOOP
            FETCH emp_cur INTO emp_rec;
            EXIT WHEN emp_cur %NOTFOUND;
            DBMS_OUTPUT.PUT_LINE(emp_rec.ename);
          END LOOP;
          CLOSE emp_cur;
        END;
        """,
        """
        DECLARE
          emp_cur REFCURSOR;
          emp_rec RECORD;
        BEGIN
          CALL get_emps(emp_cur);
          LOOP
            FETCH emp_cur INTO emp_rec;
            EXIT WHEN emp_cur NOT FOUND;
            RAISE NOTICE(emp_rec.ename);
          END LOOP;
          CLOSE emp_cur;
        END;
        """
    ),
    # 4. Процедура с IN OUT параметром курсора
    (
        """
        CREATE PROCEDURE open_emp_cur(p_dept IN NUMBER, p_cur IN OUT SYS_REFCURSOR) IS
        BEGIN
          OPEN p_cur FOR SELECT * FROM emp WHERE deptno = p_dept;
        END;
        """,
        """
        CREATE PROCEDURE open_emp_cur(p_dept IN NUMBER, INOUT p_cur REFCURSOR) IS
        BEGIN
          OPEN p_cur FOR SELECT * FROM emp WHERE deptno = p_dept;
        END;
        """
    ),
    # 5. Сложный случай с несколькими курсорами
    (
        """
        DECLARE
          cur1 SYS_REFCURSOR;
          cur2 SYS_REFCURSOR;
          r1 emp%ROWTYPE;
          r2 dept%ROWTYPE;
        BEGIN
          cur1 := get_emps();
          cur2 := get_depts();
          
          LOOP
            FETCH cur1 INTO r1;
            EXIT WHEN cur1 %NOTFOUND;
            DBMS_OUTPUT.PUT_LINE(r1.ename);
          END LOOP;
          
          LOOP
            FETCH cur2 INTO r2;
            EXIT WHEN cur2 %NOTFOUND;
            DBMS_OUTPUT.PUT_LINE(r2.dname);
          END LOOP;
          
          CLOSE cur1;
          CLOSE cur2;
        END;
        """,
        """
        DECLARE
          cur1 REFCURSOR;
          cur2 REFCURSOR;
          r1 RECORD;
          r2 RECORD;
        BEGIN
          CALL get_emps(cur1);
          CALL get_depts(cur2);
          
          LOOP
            FETCH cur1 INTO r1;
            EXIT WHEN cur1 NOT FOUND;
            RAISE NOTICE(r1.ename);
          END LOOP;
          
          LOOP
            FETCH cur2 INTO r2;
            EXIT WHEN cur2 NOT FOUND;
            RAISE NOTICE(r2.dname);
          END LOOP;
          
          CLOSE cur1;
          CLOSE cur2;
        END;
        """
    ),
    # 6. Случай без изменений (нет REFCURSOR)
    (
        """
        CREATE FUNCTION get_count RETURN NUMBER IS
          cnt NUMBER;
        BEGIN
          SELECT COUNT(*) INTO cnt FROM emp;
          RETURN cnt;
        END;
        """,
        """
        CREATE FUNCTION get_count RETURN NUMBER IS
          cnt NUMBER;
        BEGIN
          SELECT COUNT(*) INTO cnt FROM emp;
          RETURN cnt;
        END;
        """
    )
]

@pytest.mark.parametrize("oracle_code,expected_postgres", TEST_CASES)
def test_refcursor(oracle_code, expected_postgres):
    result = refcursor(oracle_code)
    assert result.strip() == expected_postgres.strip()

# Дополнительные тесты для edge cases
def test_empty_input():
    assert refcursor("") == ""

def test_no_refcursor():
    code = "BEGIN NULL; END;"
    assert refcursor(code) == code

def test_multiple_spaces():
    code = "DECLARE  cur  SYS_REFCURSOR; BEGIN  OPEN  cur  FOR  SELECT 1; END;"
    expected = "DECLARE  cur  REFCURSOR; BEGIN  OPEN  cur  FOR  SELECT 1; END;"
    assert refcursor(code) == expected

def test_case_insensitivity():
    code = "DECLARE cur Sys_Refcursor; BEGIN OPEN cur FOR SELECT 1; END;"
    expected = "DECLARE cur REFCURSOR; BEGIN OPEN cur FOR SELECT 1; END;"
    assert refcursor(code) == expected