#usando re-search() com startswith()
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
   # if re.search  ('^From:',line) :
    if line.startswith('From:') :
       print(line)