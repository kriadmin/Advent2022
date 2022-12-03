'''
    rock = 1
    paper = 2
    scissor = 3


    Them    - US
    paper   - rock    = 1 #LOSE
    rock    - paper   = 2 #WIN
    scissor - rock    = 2 #WIN
    rock    - scissor = 1 #LOSE
    paper   - scissor = 2 #WIN
    scissor - paper   = 1 #LOSE

    therefore,

    (them-us)%3 = 1 => LOSE
                = 2 => WIN
    mod == 0 => score = 3
    mod == 1 => score = 0
    mod == 2 => score = 6
'''
def score_on_mod(val):
    if(val == 0): return 3
    elif (val == 1): return 0
    else: return 6
with open("input.txt") as f:
    scores = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}
    data = f.read()
    rounds = data.split("\n")
    rounds = map(lambda x: [scores[a] for a in x.split(" ")], rounds)
    rounds = map(lambda x: sum(  [  score_on_mod((x[0] - x[1])%3)  , x[1]  ]   ),rounds)
    total_score = sum(rounds)
    print(total_score)