sum=0
for line in open("data.txt"):
    semPos=line.find(":")
    sepPos=line.find("|")
    winNums=[int(x.strip()) for x in line[semPos+1:sepPos].split()]
    cardNums=[int(x.strip()) for x in line[sepPos+1:].split()]
    intersect=list(set(winNums)&set(cardNums))
    if intersect:
        sum+=2**(len(intersect)-1)
print(sum)
