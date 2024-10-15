with open("data.txt") as f:
    content = f.read()
    
blocksWithTitle=content.split('\n\n')
blocks=[b[b.find(":")+1:].strip() for b in blocksWithTitle]
blockLists=[b.split('\n') for b in blocks]
seeds=[int(x) for x in blockLists.pop(0)[0].split(" ")]
seeds=[list(range(seeds[i],seeds[i]+seeds[i+1])) for i in range(0, len(seeds), 2)]
seeds=[item for sublist in seeds for item in sublist]
blockMaps=[list(list(int(x) for x in b.split(' ')) for b in block) for block in blockLists]

loc=[]
for seed in seeds:
    val=seed
    for maps in blockMaps:
        for map in maps:
            if map[1] <= val <= map[1]+map[2]:
                val=map[0]+val-map[1]
                break
    loc.append(val)
print(min(loc))
