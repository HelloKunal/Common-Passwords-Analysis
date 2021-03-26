import sqlite3
import time
import zlib

conn = sqlite3.connect('pstorage.sqlite')
cur = conn.cursor()

cur.execute('SELECT charac, passwordcount FROM passwordcount')
pwc=dict()

print("Loaded messages=",len(pwc))

fhand = open('pline.js','w')
fhand.write('''pline = {
  "cols":[
    {"id":"","label":"Starting character","type":"string"},
    {"id":"","label":"Number of common passwords","type":"number"}],
  "rows":[\n''')
for passwords in cur :
        if(passwords[1]>3000 and passwords[0]!="'"):
             fhand.write('{"c":[{"v":"'+passwords[0]+'"},{"v":'+str(passwords[1])+'}]},\n')
fhand.write("]}")
fhand.close()

print("Output written to pline.js")
print("Open gline.htm to visualize the data")

