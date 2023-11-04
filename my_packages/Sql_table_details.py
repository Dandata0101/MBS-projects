import os
import pandas as pd
import sqlite3

def display_table_details(file_path):
    conn = sqlite3.connect(file_path)

    # Query to fetch table names
    table_query = "SELECT name FROM sqlite_master WHERE type='table';"

    # Get table names
    tables = conn.execute(table_query).fetchall()

    # Loop through tables and display column details for each table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")
        
        # Query to get column details for the table
        column_query = f"PRAGMA table_info({table_name});"
        columns = conn.execute(column_query).fetchall()
        
        # Convert column details to a DataFrame for better visualization
        columns_df = pd.DataFrame(columns, columns=[i[0] for i in conn.execute(column_query).description])
        print(columns_df)
        print()  # For separating table details

def sample_table(file_path, table_name, limit):
    conn = sqlite3.connect(file_path)
    query = f"SELECT * FROM {table_name} LIMIT {str(limit)}"  # Convert limit to a string
    sample = pd.read_sql_query(query, conn)
    conn.close()
    return sample

def run_query_from_db(file_path, query):
    conn = sqlite3.connect(file_path)
    dfquery = pd.read_sql_query(query, conn)
    conn.close()
    return dfquery