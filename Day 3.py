import re

def getSum (l0, l1, l2):
    return int(re.search("\d+",l1).group()) if re.findall("[^ \d]", l0+l1+l2) else 0

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
    match=re.search("\d+", line)
    while match:
        start=max(0, match.span()[0]-1)
        finish=min(len(line), match.span()[1]+1)
        sum+=getSum(lines[i-1][start:finish], lines[i][start:finish], lines[i+1][start:finish])
        line=(" "*(match.span()[1]-match.span()[0])).join([line[:match.span()[0]],line[match.span()[1]:]])
        match=re.search("\d+", line)
        
    i+=1        
    
print(sum)
