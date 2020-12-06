import string

content = open('input.txt', 'r').read().split("\n\n")
alpha = set(string.ascii_lowercase)
sum = 0
for group in content:
    sum += len(alpha & set(list(group)))
input(sum)