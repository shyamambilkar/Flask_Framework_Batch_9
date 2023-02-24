import sqlite3

conn = sqlite3.connect('database.db')
print('Opened database Successfully...!!')

conn.execute('CREATE TABLE students(fname TEXT, lname TEXT, address TEXT, email TEXT, mobile TEXT, designation TEXT)')
print('Table Created Successfully...!!')
conn.close()
