import pandas as pd
import sqlite3

print("started")

df = pd.read_csv("MTA_Congestion_Relief_Zone_Vehicle_Entries__Beginning_2025_20250226.csv")
df.columns = df.columns.str.strip()

connection = sqlite3.connect('congestion.db')

df.to_sql('congestion_pricing', connection, if_exists="replace")
