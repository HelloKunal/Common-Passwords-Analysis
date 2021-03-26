import sqlite3
import time
import ssl
import re
import codecs
from difflib import SequenceMatcher

conn = sqlite3.connect('pstorage.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS commonsubs ''')

cur.execute('''CREATE TABLE IF NOT EXISTS commonsubs
   (id INTEGER UNIQUE, words TEXT, rank INTEGER)''')

nu=input('How many passwords to process: ')
nu=int(nu)
n=nu

id=0
cur.execute('''SELECT id FROM commonsubs
    WHERE id=(SELECT max(id) FROM commonsubs) AND EXISTS(SELECT * FROM commonsubs);
    ''')
for data in cur:
    id=data[0]
    print(id)

somepasswords=[]
with codecs.open('realhuman_phill.txt', 'r', encoding='utf-8',
                 errors='ignore') as passwords:
    passwords.seek(90)
    i=0
    for line in passwords:
            if(nu==0):
                break
            
            nu=nu-1                
            sline=line.split('\n')
            somepasswords.append(str(sline[0]))
substring_counts=dict()

for i in range(0, len(somepasswords)):
    print(str(i*100/n)+"%")
    for j in range(i+1,len(somepasswords)):
        string1 = somepasswords[i]
        string2 = somepasswords[j]
        match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
        matching_substring=string1[match.a:match.a+match.size]
        if(matching_substring not in substring_counts):
            substring_counts[matching_substring]=1
        else:
            substring_counts[matching_substring]+=1

id+=1
for sub in substring_counts:
    if(len(sub)>=3 and substring_counts[sub]>1000):
        cur.execute('''INSERT OR IGNORE INTO commonsubs (id, words, rank)
            VALUES ( ?, ?, ?)''', ( id, sub, substring_counts[sub]))
        id+=1

passwords.close()
conn.commit()
cur.close()


