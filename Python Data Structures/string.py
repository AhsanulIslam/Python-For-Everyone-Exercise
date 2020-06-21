s = 'tree'
print(len(s))


print(s[2])

index =0
fruit ='banana'

while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index +1

for i in fruit:
    print(i)

print ("slicing - \n")
s = fruit[0:3]
print(s)
print(fruit[3:40])
print(fruit[:5])
print(fruit[5:])

print(fruit[:])

'n' in fruit

'ru' in fruit

if 'i' in fruit:
    print("found")
