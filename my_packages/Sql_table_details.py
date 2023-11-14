import sqlite3
import os
from prettytable import PrettyTable
import pandas as pd

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
        
        # Create a PrettyTable for better visualization
        columns_table = PrettyTable()
        columns_table.field_names = [i[0] for i in conn.execute(column_query).description]
        for column in columns:
            columns_table.add_row(column)
        
        # Print the table
        print(columns_table)
        print()  # For separating table details

def sample_table(file_path, table_name, limit):
    conn = sqlite3.connect(file_path)
    query = f"SELECT * FROM {table_name} LIMIT {str(limit)}"  # Convert limit to a string
    sample = pd.read_sql_query(query, conn)
    conn.close()

    # Convert the column names (Index object) to a list of strings
    columns = list(sample.columns)

    # Create a PrettyTable and add the column names
    table = PrettyTable(columns)

    # Add data to the PrettyTable
    for row in sample.itertuples(index=False):
        table.add_row(row)

    return table


def run_query_from_db(file_path, query):
    conn = sqlite3.connect(file_path)
    dfquery = pd.read_sql_query(query, conn)
    conn.close()

    # Convert the column names (Index object) to a list of strings
    columns = list(dfquery.columns)

    # Create a PrettyTable and add the column names
    table = PrettyTable(columns)

    # Add data to the PrettyTable
    for row in dfquery.itertuples(index=False):
        table.add_row(row)

    return table
