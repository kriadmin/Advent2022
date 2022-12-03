with open("input.txt") as f:
    data = f.read()
    elves = data.split("\n\n")
    elves = list(map(lambda x: sum(list(map(lambda y: int(y),x.split("\n")))), elves))
    elves.sort(reverse=True)
    print(sum(elves[0:3]))