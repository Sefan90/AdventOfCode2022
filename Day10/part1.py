def checkCycle(i,x):
    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
        return i*x
    else:
        return 0

def part1():
    file = open('input.txt','r')
    i = 1
    x = 1
    output = 0
    for row in file:
        if "addx" in row:
            i += 1
            output += checkCycle(i,x)
            i += 1
            x += int(row.split(" ")[1])
            output += checkCycle(i,x)
        else:
            i += 1
            output += checkCycle(i,x)
        if i == 220:
            break

    print(output)

part1()

