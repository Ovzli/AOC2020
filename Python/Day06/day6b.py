content = open('input.txt', 'r').read().split("\n\n")
sum = 0
for group in content:
    listOfResponseSets = [set(list(singleResponse)) for singleResponse in group.splitlines()] #set(list(singleResponse)) gets a set of all the answers from one individual
    sum += len(set.intersection(*listOfResponseSets)) #the intersection of all sets from a group will be only the elements they all share, aka all the questions everyone answered yes to. The len of that instersection is how many elements there are
input(sum)