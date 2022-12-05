import re

with open("input.txt") as f:
    stacks,moves = f.read().split("\n\n")
    num_stacks = int(stacks.split("\n")[-1].strip()[-1])
    boxes = []
    for line in stacks.split("\n")[:-1]:
        box = [line[i:i+4].strip() for i in range(0,num_stacks*4,4)]
        assert len(box) == num_stacks
        boxes.append(box)
    boxes = map(lambda x : " ".join(list(reversed(list(x)))).strip().split(" "),zip(*boxes))
    boxes = list(boxes)
    print(boxes,"\n\n")
    for move in moves.split("\n"):
        srch = re.search("[a-zA-Z ]+([0-9]+)[a-zA-Z ]+([0-9]+)[a-zA-Z ]+([0-9]+)", move)
        num = int(srch.group(1))
        from_ = int(srch.group(2))
        to = int(srch.group(3))
        to_move = boxes[from_-1][-num:]
        boxes[from_-1][-num:] = []
        boxes[to-1].extend(to_move)
    final = []
    for column in boxes:
        final.append(column[-1][1])
    print("".join(final))