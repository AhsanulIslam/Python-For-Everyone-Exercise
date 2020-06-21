import re
x = 'My favourite 2 numbers are 99 and 69'
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[a-z0-9]',x)
print(y)


 
y = re.findall('[are]+',x)
print(y)

y = re.findall('[ARE]+',x)
print(y)

x = 'My favourite 2 numbers are 99 and 69'
y = re.findall('^M.+e',x)  #greedy match prefers longest
print(y)

y = re.findall('^M.+?e',x)  #Non greedy match prefers shortest
print(y)

#email find
eml="hy, look, imon.ahsanul.islam@gmail.com official email"
#Fine-Tuning string Extraction
find= re.findall('\S+@\S+',eml)  # \S atleast one non-whitespcae character
print(find)

find = re.findall('@([^ ]*)',eml)
print(find)

eml ='stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
find = re.findall('\S+?@\S+',eml)
print(find)
