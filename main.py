import pandas as pd
import sqlite3

print("Table Creation has started")

#Load CSV and clean column names
df = pd.read_csv("MTA_Congestion_Relief_Zone_Vehicle_Entries__Beginning_2025_20250226.csv")
df.columns = df.columns.str.strip()

# Create SQLite connection with a Database
connection = sqlite3.connect('congestion.db')

# Store DataFrame into SQLite (auto-creates the table)
df.to_sql('congestion_pricing_table', connection, if_exists="replace")

print("Table is made")
#Close the connection
connection.close()