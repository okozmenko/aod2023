import math

def getPower(s):
    colors={"red": 0,"green": 0, "blue": 0}
    for tryy in [x.strip() for x in (line[line.find(":")+1:]).split(";")]:
        colorCounts = tryy.split(", ")
        for colorCount in colorCounts:
            count, color = colorCount.split(" ")
            colors[color]=max(int(count), colors[color])

    print(colors)
    return math.prod(colors.values())

sum=0
for line in open("data.txt"):
    sum+=getPower(line)
        
print(sum)
