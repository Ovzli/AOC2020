file = open('input.txt', 'r')
content = file.read().splitlines()
# vals = list(map(int, )
count = 0 
for entry in content:
    out = entry.split(' ')
    #get pieces
    limits, letter, password = out[0], out[1], out[2]

    #get limits
    splitlimits = limits.split('-')
    lower, upper = list(map(int, splitlimits))

    #get letter
    letter = letter.strip(':')

    if(password.count(letter)>=lower and password.count(letter)<=upper):
        count += 1
print
raw_input("finished")