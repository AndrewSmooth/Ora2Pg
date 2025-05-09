
sql="""CREATE OR REPLACE PROCEDURE update_salary(emp_id IN NUMBER, salary IN NUMBER) AS
BEGIN
    UPDATE employees SET salary = salary WHERE id = emp_id;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION update_salary(emp_id NUMERIC, salary NUMERIC)
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        UPDATE employees SET salary = salary WHERE id = emp_id;
#   END;
#$$;
#Результат:CREATE OR REPLACE FUNCTION update_salary(emp_id NUMERIC, salary NUMERIC)
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        UPDATE employees SET salary = salary WHERE id = emp_id;
#    END;
#$$;
#**
sql="""CREATE OR REPLACE PROCEDURE get_employee_count(count OUT NUMBER) AS
BEGIN
    SELECT COUNT(*) INTO count FROM employees;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION get_employee_count()
#RETURNS NUMERIC
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        SELECT COUNT(*) INTO count FROM employees;
#    END;
#$$;
#Результат:CREATE OR REPLACE FUNCTION get_employee_count()
#RETURNS NUMERIC
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        SELECT COUNT(*) INTO count FROM employees;
#    END;
#$$;
#**
sql="""CREATE OR REPLACE PROCEDURE get_employee_details(emp_id IN NUMBER, name OUT VARCHAR2, hire_date OUT DATE) AS
BEGIN
    SELECT employee_name, hire_date INTO name, hire_date FROM employees WHERE id = emp_id;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION get_employee_details(emp_id NUMERIC)
#RETURNS TABLE(name VARCHAR, hire_date TIMESTAMP)
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#       SELECT employee_name, hire_date INTO name, hire_date FROM employees WHERE id = emp_id;
#    END;
#$$;
#Результат:CREATE OR REPLACE FUNCTION get_employee_details(emp_id NUMERIC)
#RETURNS TABLE(name VARCHAR, hire_date TIMESTAMP)
#LANGUAGE plpgsql
#AS $$
#   BEGIN
#       SELECT employee_name, hire_date INTO name, hire_date FROM employees WHERE id = emp_id;
#    END;
#$$;
#**
sql="""CREATE OR REPLACE PROCEDURE insert_and_commit(val IN NUMBER) AS
BEGIN
    INSERT INTO test_table(value) VALUES (val);
    COMMIT;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION insert_and_commit(val NUMERIC)
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        INSERT INTO test_table(value) VALUES (val);
#        -- COMMIT; -- Committed manually if needed
#    END;
#$$;
#Результат:CREATE OR REPLACE FUNCTION insert_and_commit(val NUMERIC)
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        INSERT INTO test_table(value) VALUES (val);
#    -- COMMIT; -- Committed manually if needed
#    END;
#$$;
#**
sql="""CREATE OR REPLACE PROCEDURE dirty_format ( a IN NUMBER )AS
BEGIN
  UPDATE test
SET val = a ;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION dirty_format(a NUMERIC)
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        UPDATE test
#        SET val = a;
#    END;
#$$;
#Результат:SELECT dirty_format(a);
#CREATE OR REPLACE FUNCTION dirty_format()
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#      UPDATE test
#    SET val = a ;
#    END;
#$$;
#**
sql="""CREATE OR REPLACE PROCEDURE nested_proc AS
BEGIN
    BEGIN
        NULL;
    END;
END;"""
#Ожидаемый результат:CREATE OR REPLACE FUNCTION nested_proc()
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        BEGIN
#            NULL;
#        END;
#    END;
#$$;
#Результат:SELECT nested_proc();
#CREATE OR REPLACE FUNCTION nested_proc()
#RETURNS void
#LANGUAGE plpgsql
#AS $$
#    BEGIN
#        BEGIN
#            NULL;
#        END;
#    END;
#$$;

