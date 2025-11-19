import sqlite3
import sys
email='admin@ecomdata.com'
if len(sys.argv)>1:
    email = sys.argv[1]
conn = sqlite3.connect('ecomdata.db')
cur = conn.cursor()
cur.execute("SELECT id, nombre, email, password, activo, fecha_creacion, rol_id FROM usuarios WHERE email = ?", (email,))
row = cur.fetchone()
if row:
    print('FOUND')
    print('id:', row[0])
    print('nombre:', row[1])
    print('email:', row[2])
    print('password:', row[3])
    print('activo:', row[4])
    print('fecha_creacion:', row[5])
    print('rol_id:', row[6])
else:
    print('NOT FOUND')
conn.close()
 
# Also print all users (for debugging)
conn = sqlite3.connect('ecomdata.db')
cur = conn.cursor()
print('\n-- All users in DB --')
for r in cur.execute('SELECT id, email, password FROM usuarios'):
    print(r)
conn.close()
