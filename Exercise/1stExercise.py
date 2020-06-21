import re

handle=open('regex_sum_590387.txt')
addition =[]
n=0
for i in handle:
    digitstr=re.findall('[0-9]+',i)
    if digitstr != []:
        for i in range(0, len(digitstr)): 
            j = int(digitstr[i])
            addition.append(j)
        #print(addition)
        #print('\n')
        #n+=addition
        #print(n)
print('\nSum :',sum(addition))
    
