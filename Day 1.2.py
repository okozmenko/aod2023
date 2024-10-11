def replaceNumbers(s):
    print(s)
    numbers={"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    pLeft={}
    pRight={}
    for n in numbers:
        i=s.find(n)
        if i>-1:
            pLeft[n] = i
            
        i=s.rfind(n)
        if i>-1:
            pRight[n] = i

    if (pLeft):
        pLeftKey=sorted(pLeft, key=pLeft.get)[0]
        s=s.replace(pLeftKey, numbers[pLeftKey])
    if (pRight):
        pRightKey=sorted(pRight, key=pRight.get)[-1]
        s=s.replace(pRightKey, numbers[pRightKey])
    
    return s
    
# -------------
sum=0
for line in open("data.txt"):
    l=replaceNumbers(line.strip())
    l=[x for x in list(l) if x.isnumeric()]

    sum+=int(l[0]+l[-1])
print(sum)
