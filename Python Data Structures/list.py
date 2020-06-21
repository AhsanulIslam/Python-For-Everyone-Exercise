friend = [1,2,4,'imon',4]

for friends in range(len(friend)):
    print(friend)


friend.append('shanin')
print(friend)


print(friend[1:2])
print(friend[0:3])

friend=['imon','afif','Shanin','Zahin','Dip']
friend.sort()
print(friend)

num =[5,6,4,3,1,8,9]
print(len(num))
print(max(num))
print(min(num))
sm = sum(num)
print(sm)
print("Average = ",sm/len(num))

numlist = list()
while True:
    inp = input('Enter numbers, done for End : ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

avg = sum(numlist)/len(numlist)
print(avg)

print('*********************Split a sentence*********************')
sentence = 'A Nation Full with bloody People'
sp = sentence.split()
print(sp)
print(len(sp))
print(sp[2])

for s in sp:
    print(s)

print('****************Range**************')

a =[2,3]
b=[3,5]
c=a+b
print(len(c))
