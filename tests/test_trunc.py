import functions.trunc as trunc

sql = "SELECT trunk(order_date, 'year') FROM orders"
converted = trunc.convert_trunk_to_date_trunc(sql)
# Результат: "SELECT date_trunc('year', order_date) FROM orders"

sql = "SELECT trunk( created_at , 'mm' ) FROM users"
converted = trunc.convert_trunk_to_date_trunc(sql)
# Результат: "SELECT date_trunc('month', created_at) FROM users"

sql = """SELECT 
    trunk(timestamp, 'yyyy') as year,
    trunk(timestamp, 'month') as month
FROM events"""
converted = trunc.convert_trunk_to_date_trunc(sql)
# Результат:
# """SELECT
#     date_trunc('year', timestamp) as year,
#     date_trunc('month', timestamp) as month
# FROM events"""

sql = "UPDATE stats SET period = trunk(log_time, 'day') WHERE id = 1"
converted = trunc.convert_trunk_to_date_trunc(sql)
# Результат: "UPDATE stats SET period = date_trunc('day', log_time) WHERE id = 1"

sql = "SELECT trunk(event_time, 'hh'), trunk(event_time, 'ww') FROM logs"
converted = trunc.convert_trunk_to_date_trunc(sql)
# Результат: "SELECT date_trunc('hour', event_time), date_trunc('week', event_time) FROM logs"