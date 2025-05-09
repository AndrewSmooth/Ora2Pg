from functions.add_months import convert_oracle_add_months_to_postgresql

oracle_query = "SELECT ADD_MONTHS(order_date, 3) FROM orders;"
postgresql_query = convert_oracle_add_months_to_postgresql(oracle_query)
print(postgresql_query)
# Вывод: SELECT (order_date + INTERVAL '3 months') FROM orders;


from functions.add_months import convert_oracle_add_months_to_postgresql

oracle_query = """
UPDATE employees 
SET contract_end = ADD_MONTHS(SYSDATE, 12) 
WHERE department = 'IT';
"""
postgresql_query = convert_oracle_add_months_to_postgresql(oracle_query)
print(postgresql_query)
# Вывод:
# UPDATE employees
# SET contract_end = (SYSDATE + INTERVAL '12 months')
# WHERE department = 'IT';


from functions.add_months import convert_oracle_add_months_to_postgresql

oracle_query = """
SELECT 
    employee_name,
    ADD_MONTHS(hire_date, 6) AS probation_end,
    ADD_MONTHS(hire_date, 12*5) AS five_years
FROM employees;
"""
postgresql_query = convert_oracle_add_months_to_postgresql(oracle_query)
print(postgresql_query)
# Вывод:
# SELECT
#     employee_name,
#     (hire_date + INTERVAL '6 months') AS probation_end,
#     (hire_date + INTERVAL '12*5 months') AS five_years
# FROM employees;


from functions.add_months import convert_oracle_add_months_to_postgresql

oracle_query = """
SELECT * FROM invoices
WHERE due_date < ADD_MONTHS(CURRENT_DATE, -1);
"""
postgresql_query = convert_oracle_add_months_to_postgresql(oracle_query)
print(postgresql_query)
# Вывод:
# SELECT * FROM invoices
# WHERE due_date < (CURRENT_DATE + INTERVAL '-1 months');


from functions.add_months import convert_oracle_add_months_to_postgresql

oracle_query = """
SELECT 
    project_name,
    ADD_MONTHS(start_date, duration_months) AS end_date
FROM projects;
"""
postgresql_query = convert_oracle_add_months_to_postgresql(oracle_query)
print(postgresql_query)
# Вывод:
# SELECT
#     project_name,
#     (start_date + INTERVAL 'duration_months months') AS end_date
# FROM projects;
