friend = ['dip','shanin','Tanjeen','Tamjid','zahin']
for i in friend:
    print(i)

largest = None
number = [4,9,8,1,3]
for i in number:
    if largest == None:
        largest=i
    elif largest < i:
        largest =i
print(largest)
                
            
            
##    print(k)
##            print ("j is ",j,"\n")
##        else:
##            print ("i is ",i,"\n")
##print("Largest Number is ",r)
total=count =0
for i in number:
    total = total+i
    count +=1
    avg=total/count
    

print("avarage =", avg)
