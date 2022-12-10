def checkCrt(i,x):
    if (i-1)%40 == x%40 or (i-1)%40 == (x+1)%40 or (i-1)%40 == (x-1)%40:
        return "#"
    return "."
    

def checkCycle(i,x):
    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
        return i*x
    else:
        return 0

def part1():
    file = open('input.txt','r')
    crt = ["." for _ in range(240)]
    i = 1
    x = 1
    output = 0
    for row in file:
        if "addx" in row:
            i += 1
            output += checkCycle(i,x)
            crt[i-1] = checkCrt(i,x)
            i += 1
            x += int(row.split(" ")[1])
            crt[i-1] = checkCrt(i,x)
            output += checkCycle(i,x)
        else:
            i += 1
            output += checkCycle(i,x)
            crt[i-1] = checkCrt(i,x)
        if i == 240:
            break

    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:240])
part1()
