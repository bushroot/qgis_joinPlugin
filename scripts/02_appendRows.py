


# Access the junction table in the sqlite DB
import sqlite3

# Define inputs
sqlite_file = "/Users/rogerbaer/OneDrive/Projects/QGIS_programming/03_explorePlugining/GIS/db_pratteln.sqlite"
table_name = 'e_pivot'
column_name_1 = 'id_weg'
column_name_2 = 'id_fb'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# List all tables from the db
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# Get Column name
cur = c.execute('select * from b_pivot')
print(cur.description)

# Add new row with values
c.execute("INSERT INTO {tn} ({c1}, {c2}) VALUES (123456, 'test')".\
     format(tn=table_name, c1=column_name_1, c2=column_name_2))

conn.commit()
conn.close()
