def rec(row,i,m):
    if i < 0:
        return 0
    elif row[i].isnumeric():
        return int(row[i])*m + rec(row,i-1,m*5)
    elif row[i] == "=":
        return -2*m + rec(row,i-1,m*5)
    elif row[i] == "-":
        return -1*m + rec(row,i-1,m*5)
    return 0

def revRec(input,d):
    


def part1():
    file = [r.replace("\n","") for r in open('input.txt','r')]
    output = 0
    for row in file:
        output += rec(row,len(row)-1,1)
    print(output)

part1()