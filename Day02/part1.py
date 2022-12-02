def part1():
    file = open('input.txt','r')
    score = 0
    for row in file:
        op, me = row.replace("\n","").split(" ")
        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        else:
            score += 3        
        
        if ord(me) - ord(op) == 23:
            score += 3
        elif ord(me) - ord(op) == 24 or ord(me) - ord(op) == 21:
            score += 6

    print(score)

part1()