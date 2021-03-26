import sqlite3
import time
import zlib

conn = sqlite3.connect('pstorage.sqlite')
cur = conn.cursor()

cur.execute('SELECT charac, passwordcount FROM passwordcount')
pwc=dict()

print("Loaded messages=",len(pwc))

fhand = open('pline.js','w')
fhand.write('pline = [ ["id", "Password starting with", "No of common passwords"]')
nu=1
for passwords in cur :
        if(passwords[1]>3000 and passwords[0]!="'"):
             fhand.write(",\n["+str(nu)+",'"+passwords[0]+"',"+str(passwords[1])+"]")
             nu+=1
fhand.write(" ]")
fhand.close()

print("Output written to pline.js")
print("Open gline.htm to visualize the data")

