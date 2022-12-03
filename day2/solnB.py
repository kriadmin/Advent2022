'''
    rock = 1
    paper = 2
    scissor = 3

    lose = 2
    draw = 0
    win = 1

    THEM - US
    rock(1) - lose(2) = scissor = 3
    rock(1) - draw(0) = rock = 1
    rock(1) - win(1) = paper = 2

    paper(2) - lose(2) = rock = 1
    and so on....
'''
def score_on_mod(val):
    if(val == 0): return 3
    elif (val == 1): return 0
    else: return 6
with open("input.txt") as f:
    scores = {"A":1,"B":2,"C":3,"X":2,"Y":0,"Z":1}
    data = f.read()
    rounds = data.split("\n")
    rounds = map(lambda x: [scores[a] for a in x.split(" ")], rounds)
    rounds = map(lambda x: sum([ (x[0]+x[1])%3 if (x[0] + x[1])%3 != 0  else 3, ((x[1] + 1)%3)*3]) ,rounds)
    total_score = sum(rounds)
    print(total_score)