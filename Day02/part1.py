def part1():
    file = open('input.txt','r')
    score = 0
    for row in file:
        tmp_score = 0
        op, me = row.replace("\n","").split(" ")
        if ord(me) == 88:
            tmp_score += 1
        elif ord(me) == 89:
            tmp_score += 2
        elif ord(me) == 90:
            tmp_score += 3        
        
        if ord(me) - ord(op) == 23:
            tmp_score += 3
        elif ord(me) - ord(op) == 24 or ord(me) - ord(op) == 21:
            tmp_score += 6
        print(tmp_score)
        score += tmp_score

    print(score)

part1()