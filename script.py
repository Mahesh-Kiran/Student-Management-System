import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Example: read data from a table
cursor.execute("SELECT * FROM Student_App_student;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
