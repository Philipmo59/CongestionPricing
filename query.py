import pandas as pd
import sqlite3

#Connect to the Database
connection = sqlite3.connect('congestion.db')

query = """
SELECT "Time Period", COUNT(*) as vechicle_count
FROM congestion_pricing_table
GROUP BY "Time Period";
"""

df_query = pd.read_sql(query,connection)

connection.close()

print(df_query)
