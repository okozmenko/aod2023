sum=0
for line in open("data.txt"):
    l=[x for x in list(line) if x.isnumeric()]
    sum+=int(l[0]+l[-1])
print(sum)
