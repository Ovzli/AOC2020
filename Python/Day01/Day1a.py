
#Quick n' dirty day 1
file = open('sortedInput.txt', 'r')
content = file.read().split()
lower, upper = list(map(int, content[:9])), list(map(int, content[9:])) # 2020 cant be the sum of two integers where x>1010 OR x<1010 is true for BOTH  
li = ui = 0 # so for efficencys sake only compare integers where it's possible for 2020 to be a sum
for l in lower:
    for u in upper:
        if (l+u==2020):
            nums = l,u
print(nums)
print(nums[0]*nums[1])
raw_input("finished")


