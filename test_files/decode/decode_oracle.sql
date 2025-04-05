SELECT employee_id, 
    DECODE(gender, 'M', 'Male', 'F', 'Female', 'Unknown') AS gender_description
FROM employees;