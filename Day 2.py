def check(s):
    colors={"red": 12,"green": 13, "blue": 14}
    for tryy in [x.strip() for x in (line[line.find(":")+1:]).split(";")]:
        colorCounts = tryy.split(", ")
        for colorCount in colorCounts:
            count, color = colorCount.split(" ")
            if int(count) > colors[color]:
                return False
                
    return True

sum=0
i=1
for line in open("data.txt"):
    if check(line):
        sum+=i
    i+=1
    
print(sum)
