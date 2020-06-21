new = dict()
new['first']=2
new['2nd']=3

print(new)
new['2nd'] = new['2nd']+1
print(new)

dic={'one':1 , 'two':2,'three':3}
print(dic)
print(dic.keys())
print(dic['one'])
print(dic.values())
print(dic.items())

for k,v in dic.items():
    print(k,v)

stuff = dict()
print(stuff.get('candy',-1))
