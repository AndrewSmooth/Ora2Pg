sql="""SELECT id, name, value
FROM products
UNPIVOT (value FOR name IN (price, weight, quantity))"""
#Ожидаемый результат: SELECT id, name, value
#FROM products
#JOIN LATERAL (VALUES
#        ('price', price),
#        ('weight', weight),
#        ('quantity', quantity)
#    ) AS unpivoted(name, value) ON true
#Результат:SELECT id, name, value
#FROM products
#JOIN LATERAL (VALUES
#        ('price', price),
#        ('weight', weight),
#        ('quantity', quantity)
#    ) AS unpivoted(name, value) ON true
#**
sql="""SELECT emp_id, metric_type, metric_value
FROM employee_stats
UNPIVOT (
    metric_value FOR metric_type IN (
        sales AS 'TOTAL_SALES', 
        hours AS 'WORK_HOURS'
    )
)"""
#Ожидаемый результат:SELECT emp_id, metric_type, metric_value
#FROM employee_stats
#JOIN LATERAL (VALUES
#        ('TOTAL_SALES', sales),
#        ('WORK_HOURS', hours)
#    ) AS unpivoted(metric_type, metric_value) ON true
#Результат:SELECT emp_id, metric_type, metric_value
#FROM employee_stats
#JOIN LATERAL (VALUES
#        ('TOTAL_SALES', sales),
#        ('WORK_HOURS', hours)
#    ) AS unpivoted(metric_type, metric_value) ON true
#**
sql="""SELECT id, k, v
FROM data
UNPIVOT (
    v FOR k IN (
        col1 AS 'c1',
        col2 AS 'c2',
        col3 AS 'c3'
    )
) WHERE id > 100"""
#Ожидаемый результат:SELECT id, k, v
#FROM data
#JOIN LATERAL (VALUES
#        ('c1', col1),
#       ('c2', col2),
#        ('c3', col3)
#    ) AS unpivoted(k, v) ON true
#WHERE id > 100
#Результат:SELECT id, k, v
#FROM data
#JOIN LATERAL (VALUES
#        ('c1', col1),
#        ('c2', col2),
#        ('c3', col3)
#    ) AS unpivoted(k, v) ON true WHERE id > 100
#**
sql="""SELECT a, b FROM t UNPIVOT (b FOR a IN (x, y, z))
SELECT a, b FROM t
JOIN LATERAL (VALUES
        ('x', x),
        ('y', y),
        ('z', z)
    ) AS unpivoted(a, b) ON true"""
#Ожидаемый результат:SELECT a, b FROM t
#JOIN LATERAL (VALUES
#        ('x', x),
#        ('y', y),
#        ('z', z)
#    ) AS unpivoted(a, b) ON true
#Результат:SELECT a, b FROM t
#JOIN LATERAL (VALUES
#        ('x', x),
#       ('y', y),
#        ('z', z)
#    ) AS unpivoted(a, b) ON true
sql="""SELECT * FROM dataset
UNPIVOT (
    val FOR col IN (
        "col1" AS 'Column1', 
        col2, 
        col3 AS 'Third_Column'
    )
)"""
#Ожидаемый результат:SELECT * FROM dataset
#JOIN LATERAL (VALUES
#        ('Column1', col1),
#        ('col2', col2),
#        ('Third_Column', col3)
#    ) AS unpivoted(col, val) ON true
#Результат:SELECT * FROM dataset
#JOIN LATERAL (VALUES
#        ('Column1', col1),
#        ('col2', col2),
#        ('Third_Column', col3)
#    ) AS unpivoted(col, val
