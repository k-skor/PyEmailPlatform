import sqlite3

conn = sqlite3.connect('contacts.db')
cur = conn.cursor()
cur.execute('SELECT * FROM contact ORDER BY emailaddress')
contacts = cur.fetchall()

for contact in contacts:
    print('{0} {1} {2} {3}'.format(contact[1], contact[2], contact[3],
        contact[4]))
