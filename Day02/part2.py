def part1():
    file = open('input.txt','r')
    score = 0
    for row in file:
        tmp_score = 0
        tmp_outcome = 0
        op, me = row.replace("\n","").split(" ")        
        if me == "Y":
            tmp_score += 3
            tmp_outcome = ord(op) + 23
        elif me == "Z":
            tmp_score += 6
            tmp_outcome = ord(op) + 24
            if tmp_outcome > 90:
                tmp_outcome = 88
        else:
            tmp_outcome = ord(op) + 22
            if tmp_outcome < 88:
                tmp_outcome = 90

        if tmp_outcome == 88:
            tmp_score += 1
        elif tmp_outcome == 89:
            tmp_score += 2
        elif tmp_outcome >= 90:
            tmp_score += 3          
        score += tmp_score

    print(score)

part1()