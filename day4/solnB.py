with open("input.txt") as f:
    data = f.readlines()
    data = map(lambda x: [*map(lambda y: [*map( int, y.split("-"))],   x.split(","))], data)
    data = map(lambda x: [set(range(x[0][0],x[0][1]+1)) , set(range(x[1][0],x[1][1]+1)) ] , data)
    data = *filter(lambda x: x[0].intersection(x[1]),data),
    print(len(data))