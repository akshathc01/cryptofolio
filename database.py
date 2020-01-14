import sqlite3

con = sqlite3.connect('folio.db')

cObj = con.cursor()

# cObj.execute('CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)')
# con.commit()

# cObj.execute('INSERT INTO employees VALUES(?, ?, ?, ?, ?)', (2, 'Akshath', 50000, 'JS', 'Developer'))
# con.commit()

# cObj.execute('UPDATE employees SET department="PHP" WHERE id=2')
# con.commit()

# cObj.execute('SELECT * FROM employees')
# result = cObj.fetchall()
#
# print(result)

cObj.execute('DELETE FROM employees')
con.commit()


cObj.close()
con.close()
