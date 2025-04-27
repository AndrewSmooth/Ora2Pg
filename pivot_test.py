import pivot

if __name__ == "__main__":
    query = pivot.generate_pivot_query(
        table="sales",
        row_key="product",
        pivot_column="region",
        value_column="amount",
        pivot_values=["North", "South"],
        agg_func="SUM"
    )

    print("-- Установите расширение если нужно:")
    print("CREATE EXTENSION IF NOT EXISTS tablefunc;\n")
    print("-- SQL запрос:")
    print(query)
