def checkTail(hx,hy,tx,ty):
    if (tx-hx == 1 and ty-hy > 1) or (tx-hx > 1 and ty-hy == 1):
        return -1,-1
    elif (tx-hx == -1 and ty-hy > 1) or (tx-hx < -1 and ty-hy == 1):
        return 1,-1
    elif (tx-hx == 1 and ty-hy < -1) or (tx-hx > 1 and ty-hy == -1):
        return -1,1
    elif (tx-hx == -1 and ty-hy < -1) or (tx-hx < -1 and ty-hy == -1):
        return 1,1
    elif tx-hx > 1:
        return -1,0
    elif tx-hx < -1:
        return 1,0
    elif ty-hy > 1:
        return 0,-1
    elif ty-hy < -1:
        return 0,1
    else:
        return 0,0

def part1():
    file = open('input.txt','r')
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    head = [[hx,hy]]
    tail = set()
    for row in file:
        if "U" in row:
            for _ in range(int(row.split(" ")[1])):
                hy += 1
                head.append([hx,hy])
                tmptx,tmpty = checkTail(hx,hy,tx,ty)
                tx += tmptx
                ty += tmpty
                tail.add(str(tx)+" "+str(ty))
        elif "D" in row:
            for _ in range(int(row.split(" ")[1])):
                hy -= 1
                head.append([hx,hy])
                tmptx,tmpty = checkTail(hx,hy,tx,ty)
                tx += tmptx
                ty += tmpty
                tail.add(str(tx)+" "+str(ty))
        elif "L" in row:
            for _ in range(int(row.split(" ")[1])):
                hx -= 1
                head.append([hx,hy])
                tmptx,tmpty = checkTail(hx,hy,tx,ty)
                tx += tmptx
                ty += tmpty
                tail.add(str(tx)+" "+str(ty))
        elif "R" in row:
            for _ in range(int(row.split(" ")[1])):
                hx += 1
                head.append([hx,hy])
                tmptx,tmpty = checkTail(hx,hy,tx,ty)
                tx += tmptx
                ty += tmpty
                tail.add(str(tx)+" "+str(ty))

    print(len(tail))

part1()

