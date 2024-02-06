import pandas as pd
import mysql.connector
from datetime import datetime, timedelta

def export_mysql_data_to_csv(host, user, password, database, table, start_date, end_date=None, output_filename="exported_data.csv"):
    """
    Export data from a MySQL table to a CSV file within a specified date range.

    Args:
        host (str): The MySQL server hostname or IP address.
        user (str): The MySQL username for authentication.
        password (str): The MySQL password for authentication.
        database (str): The name of the MySQL database containing the table.
        table (str): The name of the table from which data will be exported.
        start_date (datetime): The start date (inclusive) for the data export.
        end_date (datetime, optional): The end date (inclusive) for the data export.
            If not provided, the current date will be used as the end date.
        output_filename (str, optional): The name of the CSV file to which the data will be exported.
            Defaults to "exported_data.csv".

    Returns:
        None: The function exports the data to the specified CSV file.
    """
    # If end_date is not provided, use the current date as the default
    if end_date is None:
        end_date = datetime.now()

    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Format the start and end dates
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    # Construct the SQL query to select data within the date range
    query = f"SELECT * FROM {table} WHERE date >= '{start_date}' AND date <= '{end_date}'"

    # Execute the query and load the data into a DataFrame
    df = pd.read_sql(query, con=connection)

    # Export the data to a CSV file
    df.to_csv(output_filename, index=False)

    # Close the database connection
    connection.close()
