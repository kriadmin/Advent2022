with open("input.txt") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
    data = [data[i:i+3] for i in range(0,len(data),3)]
    data = map(lambda x: set(x[0]).intersection(set(x[1]).intersection(set(x[2]))).pop()  ,data)
    data = map(lambda x: ord(x) - 96 if x.islower() else ord(x) - 38, data)
    print(sum(data))