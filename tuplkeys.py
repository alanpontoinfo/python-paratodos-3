number_strings= ['1','2','3','4']
number_ints=[]
#directory[last, first] = number

for x in number_strings :
    number_ints.append(int(x))
     #print(first, last, directory[last,first])
print(sum(number_ints))