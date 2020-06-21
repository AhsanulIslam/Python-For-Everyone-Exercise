##5.2 Write a program that repeatedly prompts a user
##for integer numbers until the user enters 'done'

##Once 'done' is entered, print out the largest and smallest of the numbers.
##If the user enters anything other than a valid number catch it with atry/except
##and
##put out an appropriate message and ignore the number.
##Enter 7, 2, bob, 10, and 4 and
##match the output below


largest = None
smallest = None
invalid = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        i = int(num)
    except:
        invalid ='Invalid input'
        continue
    if largest == None:
        largest = i
    elif largest < i:
        largest = i
        
    if smallest == None:
        smallest = i
    elif smallest > i:
        smallest = i
    

print(invalid)
print("Maximum is", largest)
print("Minimum is", smallest)
