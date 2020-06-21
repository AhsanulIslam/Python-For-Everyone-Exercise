handle = open('file.txt')
print(handle)
count =0
##for cheese in handle:
##    count=count+1
##    print(cheese)
##print("Line Count : ",count)

##inp = handle.read()
##print(len(inp))


for line in handle:
    line = line.rstrip()
    if line.startswith('hello '):
        print(line)
