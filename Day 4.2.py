with open("data.txt") as f:
    lines = f.readlines()
    
cardCopies=[1]*len(lines)
i=0
while i < len(lines)-1:
    line=lines[i]
    semPos=line.find(":")
    sepPos=line.find("|")
    winNums=[int(x.strip()) for x in line[semPos+1:sepPos].split()]
    cardNums=[int(x.strip()) for x in line[sepPos+1:].split()]
    winCount=len(list(set(winNums)&set(cardNums)))

    if winCount:
        j=1
        while j <= winCount:
            if ((i+j)>len(cardCopies)-1):
                break
            cardCopies[i+j]+=cardCopies[i]
            j+=1
    
    i+=1

print(sum(cardCopies))
