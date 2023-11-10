import teradatasql
import pandas as pd

# Teradata connection parameters
host = "your_teradata_host"
user = "your_username"
password = "your_password"
database = "your_database"

# Connection string
connection_string = f"DRIVER={{Teradata Driver}};DBCNAME={host};UID={user};PWD={password};DATABASE={database};"

# Establish a connection
con = teradatasql.connect(connection_string)

# Cursor to execute SQL statements
cur = con.cursor()

# Table and file information
table_name = "your_table"
csv_file = "your_data.csv"

# SQL statement to load data
sql = f"COPY {table_name} FROM {csv_file} USING CLIENT CHARSET 'UTF8' DELIMITER ','"

# Execute the SQL statement
cur.execute(sql)

# Commit the transaction
con.commit()

# Close the cursor and connection
cur.close()
con.close()
