content = open('input.txt', 'r').read().split("\n\n")
validCount = 0
reqFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
for entry in content:
    if all(x in entry for x in reqFields):
        validCount += 1
print(validCount)
print(int("test:12"))
raw_input("finished")