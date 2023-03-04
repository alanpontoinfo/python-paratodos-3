han = open('teste3.txt')

for line in han:
 line = line.rstrip()
 wds = line.split()
 #print('Line:', line)
 #if line == '':
 # print('skip blank')
  #continue
 
 #print('Words:' , wds)
 #guardiao
 #if len(wds) < 1 :
  #continue
 #if wds[0] != 'From' :
 # print('ignore')
  #continue

 if len(wds) < 3 or wds[0] != 'From' :
  continue
 print(wds[2])