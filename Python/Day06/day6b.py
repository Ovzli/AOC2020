content = open('input.txt', 'r').read().split("\n\n")
sum = 0
for group in content:
    sets = [set(list(person)) for person in group.splitlines()]
    sum += len(set.intersection(*sets))
input(sum)