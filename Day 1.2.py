def replaceNumbers(s):
    numbers={"one": "o1e", "two": "t2o", "three": "t3e", "four": "4", "five": "5e", "six": "6", "seven": "7n", "eight": "e8t", "nine": "n9e"}
    
    i = 0
    while i < len(s)-1:
        part1=s[:i]
        part2=s[i:]

        pos=-1
        for n in numbers:
            pos=part2.find(n)
            if pos==0:
                part2=part2.replace(n, numbers[n], 1)
                break
                
        i+=1
        s=part1+part2

    return s
    
# -------------
sum=0
for line in open("data.txt"):
    l=replaceNumbers(line.strip())
    l=[x for x in list(l) if x.isnumeric()]
    sum+=int(l[0]+l[-1])
print(sum)
