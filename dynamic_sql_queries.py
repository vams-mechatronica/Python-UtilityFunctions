import sqlite3


def run_dynamic_query(table_name, column_values):
    # Connect to the database
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Build the SQL query dynamically based on the table name and column values
    columns = ', '.join(column_values.keys())
    values = ', '.join('?' * len(column_values))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

    # Execute the SQL query with the column values as parameters
    c.execute(sql, list(column_values.values()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
