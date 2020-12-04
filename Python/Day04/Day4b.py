import re

def CheckValidity(passport):
    reqFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    valid = all(x in passport for x in reqFields)
    if (not valid):
        return valid
    for entry in re.split(r" |\n",passport): # What have I done
        valid = valid and (
            (bool(re.search(r"byr:\d{4}\b", entry)) and ((1920 <= int(re.sub('[^0-9]',"",entry))) and (int(re.sub('[^0-9]',"",entry)) <= 2002)))
            or (bool((re.search(r"iyr:\d{4}\b", entry))) and (2010 <= int(re.sub('[^0-9]',"",entry)) <= 2020))
            or (bool((re.search(r"eyr:\d{4}\b", entry))) and (2020 <= int(re.sub('[^0-9]',"",entry)) <= 2030))
            or (bool(re.search(r"hcl:#[0-9a-f]{6}\b", entry)))
            or (bool(re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", entry)))
            or (bool(re.search(r"pid:\d{9}\b", entry)))
            or (bool((re.search(r"hgt:\d{3}cm\b", entry))) and (150 <= int(re.sub('[^0-9]',"",entry)) <= 193))
            or (bool((re.search(r"hgt:\d{2}in\b", entry))) and (59 <= int(re.sub('[^0-9]',"",entry)) <= 76))
            or (bool(re.search(r"cid",entry)))
            )
    return valid



content = open('input.txt', 'r').read().split("\n\n")
validCount = 0

for entry in content:
    if CheckValidity(entry):
        validCount += 1
print(validCount)
raw_input("finished")