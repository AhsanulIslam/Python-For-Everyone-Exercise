fh = open('mbox-short.txt')
tot = 0
ans = 0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
ans = tot / count
print("Average spam confidence:", ans)
