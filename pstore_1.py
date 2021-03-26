import sqlite3
import time
import ssl
import re
import codecs

conn = sqlite3.connect('pstoreage.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS passwords ''')
cur.execute('''CREATE TABLE IF NOT EXISTS passwords
    (id INTEGER UNIQUE, pass TEXT, passwordcount INTEGER)''')

#cur.execute('''CREATE TABLE IF NOT EXISTS commonsubs
#    (id INTEGER UNIQUE, rank INTEGER UNIQUE, words TEXT)''')

nu=1
with codecs.open('realhuman_phill.txt', 'r', encoding='utf-8',
                 errors='ignore') as passwords:
    passwords.seek(90)
    for line in passwords:
        try:
            sline=line.split('\n')
            pc=len(sline[0])
            cur.execute('''INSERT OR IGNORE INTO passwords (id, pass, passwordcount)
                VALUES ( ?, ?, ?)''', ( nu, sline[0], pc))
            nu+=1
            if(nu%10000000==0):
                print('10000000Done!\n')
                conn.commit()
        except:
            pass

passwords.close()
conn.commit()
cur.close()
