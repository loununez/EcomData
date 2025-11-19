import sqlite3
import sys
import bcrypt

if len(sys.argv) < 3:
    print('Usage: create_user.py <email> <password> [nombre] [rol_id]')
    sys.exit(1)

email = sys.argv[1]
password = sys.argv[2]
nombre = sys.argv[3] if len(sys.argv) > 3 else 'Admin'
rol_id = int(sys.argv[4]) if len(sys.argv) > 4 else 1

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

conn = sqlite3.connect('ecomdata.db')
cur = conn.cursor()
# Check existing
cur.execute('SELECT id FROM usuarios WHERE email = ?', (email,))
if cur.fetchone():
    print('User already exists')
else:
    cur.execute('INSERT INTO usuarios (nombre,email,password,activo,fecha_creacion,rol_id) VALUES (?,?,?,?,datetime("now"),?)', (nombre,email,hashed,1,rol_id))
    conn.commit()
    print('User created:', email)
conn.close()
