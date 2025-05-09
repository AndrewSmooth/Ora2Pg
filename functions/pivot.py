def generate_pivot_query(
        table: str,
        row_key: str,
        pivot_column: str,
        value_column: str,
        pivot_values: list,
        agg_func: str = "SUM"
) -> str:
    """
    Генерирует PostgreSQL crosstab запрос из параметров, аналогичных Oracle PIVOT

    :param table: Имя таблицы
    :param row_key: Столбец для строк (например, product)
    :param pivot_column: Столбец для сводных заголовков (например, region)
    :param value_column: Значения для агрегации
    :param pivot_values: Список значений для столбцов
    :param agg_func: Агрегатная функция (SUM, AVG и т.д.)
    :return: SQL-запрос в виде строки
    """
    # Экранирование специальных символов
    safe_values = [v.replace("'", "''") for v in pivot_values]

    # Формирование значений для второго параметра crosstab
    values_sql = ", ".join(f"('{v}')" for v in safe_values)

    # Формирование структуры результата
    columns_sql = ", ".join(
        [f'"{row_key}" TEXT'] +
        [f'"{val}" NUMERIC' for val in pivot_values]
    )

    return f"""
    SELECT * 
    FROM crosstab(
        $$SELECT 
            "{row_key}", 
            "{pivot_column}", 
            {agg_func}("{value_column}") 
         FROM "{table}" 
         GROUP BY "{row_key}", "{pivot_column}" 
         ORDER BY 1, 2$$,
        $$VALUES {values_sql}$$
    ) AS ct({columns_sql});
    """
