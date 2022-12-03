with open("input.txt") as f:
    data = f.readlines()
    data = map(lambda x: set(x[:len(x)//2]).intersection(x[len(x)//2:]).pop() , data)
    data = map(lambda x: ord(x) - 96 if x.islower() else ord(x) - 38, data)
    print(sum(data))