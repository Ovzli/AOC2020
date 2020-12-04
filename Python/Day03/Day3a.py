file = open('input.txt', 'r')
content = file.read().splitlines()
xpos = 0
treeCount = 0
for line in content:
    if(line[xpos] == "#"):
        treeCount += 1
    xpos += 3
    xpos = xpos % len(line)
print(treeCount)
raw_input("finished")