def countTrees(xslope,yslope,map):
    xpos = ypos = treeCount = 0
    lineLen = len(map[0])
    while(ypos < len(map)):
        if(map[ypos][xpos] == "#"):
            treeCount += 1
        xpos = (xpos+xslope) % lineLen
        ypos += yslope
    return treeCount

file = open('input.txt', 'r')
content = file.read().splitlines()
s1 = countTrees(1,1,content)
s2 = countTrees(3,1,content)
s3 = countTrees(5,1,content)
s4 = countTrees(7,1,content)
s5 = countTrees(1,2,content)
print(s1*s2*s3*s4*s5)
raw_input("finished")