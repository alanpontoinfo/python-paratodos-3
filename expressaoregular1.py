import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
    #if line.find('From:') >= 0:
       print(line)