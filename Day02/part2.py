def outcome(tmp_outcome):
    if tmp_outcome == 88 or tmp_outcome > 90:
        return(1)
    elif tmp_outcome == 89:
        return(2)
    elif tmp_outcome == 90 or tmp_outcome < 88:
        return(3)  

def part2():
    file = open('input.txt','r')
    score = 0
    for row in file:
        op, me = row.replace("\n","").split(" ")        
        if me == "Y":
            score += outcome(ord(op) + 23) + 3
        elif me == "Z":
            score += outcome(ord(op) + 24) + 6
        else:
            score += outcome(ord(op) + 22)

    print(score)

part2()