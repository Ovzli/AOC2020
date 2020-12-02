file = open('sortedInput.txt', 'r')
content = file.read().split()
vals = list(map(int, content))
for v1 in vals:
    v2start = vals.index(v1) # Why not add some efficiency? 
    for v2 in vals[v2start:]:
        v3start = vals.index(v2)
        for v3 in vals[v3start:]:
            if (v1+v2+v3 == 2020):
                nums = v1,v2,v3
print(nums)
print(nums[0]*nums[1]*nums[2])
raw_input("finished")
