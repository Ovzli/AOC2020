file = open('input.txt', 'r')
content = file.read().splitlines()
# vals = list(map(int, )
count = 0 
for entry in content:
    out = entry.split(' ')
    #get pieces
    pos, letter, password = out[0], out[1], out[2]

    #get limits
    first, last = list(map(int, pos.split('-')))

    #get letter
    letter = letter.strip(':')

    if((password[first-1] == letter) ^ (password[last-1] == letter)):
        count += 1
print(count)
raw_input("finished")