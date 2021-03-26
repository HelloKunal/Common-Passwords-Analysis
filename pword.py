import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('pstorage.sqlite')
cur = conn.cursor()

# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('SELECT words, rank FROM commonsubs ORDER BY rank DESC')
counts = dict()
highest = None
lowest = None
i=0
for word_row in cur :
    if(i==200):
        break
    counts[word_row[0]]=word_row[1]
    if highest is None or highest < word_row[1] :
        highest = word_row[1]
    if lowest is None or lowest > word_row[1] :
        lowest = word_row[1]
    i+=1

print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('pword.js','w')
fhand.write("pword = [")
first = True
for word_row in counts:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[word_row]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+word_row+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open pword.htm in a browser to see the vizualization")
