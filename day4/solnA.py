with open("input.txt") as f:
    data = f.readlines()
    data = map(lambda x: [*map(lambda y: [*map( int, y.split("-"))],   x.split(","))], data)
    containsA = lambda x , y , z,  w : x >= z and y <= w 
    containsB = lambda a , b : containsA(a[0] , a[1] , b[0] , b[1])
    data = *filter(lambda x: containsB(x[0], x[1]) or containsB(x[1], x[0]), data),
    print(len(data))