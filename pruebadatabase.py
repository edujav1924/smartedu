import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table

# Insert a row of data
#c.execute("INSERT INTO COMPANY (status,hora) VALUES ( 15, 'hora')")
c.execute('''SELECT status FROM tempe''')
user1 = c.fetchall() #retrieve the first row
print(len(user1)) #Print the first column retrieved(user's name)
print(user1[len(user1)-1][0])
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
