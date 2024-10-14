import re

def getRatio(l0, l1, l2, pos):
    set=[]
    for line in [l0, l1, l2]:
        match=re.search("\d+", line)
        while match:
            if (match.span()[0]<=pos+1) and (match.span()[1]-1>=pos-1):
                set.append(int(match.group()))
            
            line=(" "*(match.span()[1]-match.span()[0])).join([line[:match.span()[0]],line[match.span()[1]:]])
            match=re.search("\d+", line)
    
    if len(set) == 2:
        return set[0]*set[1]
    else:
        return 0

with open("data.txt") as f:
    lines = f.readlines()
lines = [l.strip().replace(".", " ") for l in lines]
emptyLine=" "*len(lines[0])
lines.insert(0, emptyLine)
lines.append(emptyLine)
    
sum=0
i=1
while i < len(lines)-1:
    line=lines[i]
    match=re.search("\*", line)
    while match:
        sum+=getRatio(lines[i-1], lines[i], lines[i+1], match.span()[0])
        
        lineList = list(line)
        lineList[match.span()[0]]=" "
        line="".join(lineList)
        
        match=re.search("\*", line)
        
    i+=1        
    
print(sum)
