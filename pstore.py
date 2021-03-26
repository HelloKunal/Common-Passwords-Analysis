import sqlite3
import time
import ssl
import re
import codecs

conn = sqlite3.connect('pstorage.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS passwords ''')
cur.execute('''DROP TABLE IF EXISTS passwordcount ''')
cur.execute('''CREATE TABLE IF NOT EXISTS passwordcount
    (charac CHAR(1) UNIQUE, passwordcount INTEGER)''')

#cur.execute('''CREATE TABLE IF NOT EXISTS commonsubs
#    (id INTEGER UNIQUE, rank INTEGER UNIQUE, words TEXT)''')

pct=0
with codecs.open('realhuman_phill.txt', 'r', encoding='utf-8',
                 errors='ignore') as passwords:
        passwords.seek(91)
        chara=dict()
        for line in passwords:
                sline=line.split('\n')
                try:
                        if(sline[0][0] in chara):
                                chara[sline[0][0]]=chara[sline[0][0]]+1
                        else:
                                chara[sline[0][0]]=0
                                print(sline[0][0], ' Done!')
                except:
                        pass

for char in sorted(chara.keys()):
        cur.execute('''INSERT OR IGNORE INTO passwordcount (charac, passwordcount)
                VALUES ( ?, ?)''', ( char, chara[char]))
passwords.close()
conn.commit()
cur.close()
