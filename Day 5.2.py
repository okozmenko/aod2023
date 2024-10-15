with open("data1.txt") as f:
    content = f.read()
    
blocksWithTitle=content.split('\n\n')
blocks=[b[b.find(":")+1:].strip() for b in blocksWithTitle]
blockLists=[b.split('\n') for b in blocks]
seeds=[int(x) for x in blockLists.pop(0)[0].split(" ")]
seeds=[[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

blockMaps=[list(list(int(x) for x in b.split(' ')) for b in block) for block in blockLists]

print(seeds)
print(blockMaps)

# loc=[]
# for seed in seeds:
#     val=seed
#     for maps in blockMaps:
#         for map in maps:
#             if map[1] <= val <= map[1]+map[2]:
#                 val=map[0]+val-map[1]
#                 break
#     loc.append(val)
# print(min(loc))

def chunkOverlap(range, map):
    start1, end1=[range[0], range[0]+range[1]]
    destination, start2, end2 =[range[0], [range[1], range[1]+range[2]],
    
    if !((start1<=end1) and (end1>=start2)): # no overlap
        return [range]

    # overlap
    startOverlap=max(start1, start2)
    endOverlap=min(end1, end2)
    newRanges.append([destination+startOverlap-start2, endOverlap-startOverlap])
        
    # if ((start1>=start2) and (end1<=end2)): # full overlap
    #     return [[destination+start1-start2, range[1]]]
        
    newRanges=[]
    if ((start1<start2): # have a piece left
        newRanges.append([start1, start2-start1])
        
    if ((end2<end1): # have a piece right
        newRanges.append([end2, end2-end1])
        

    return (range1[0]<=range2[0]+range2[1]) and (range1[0]+range1[1]>=range2[0])
    
print(hasOverlap([3,1],[5,4]))
