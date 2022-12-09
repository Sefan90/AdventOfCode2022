def checkTail(hx,hy,tx,ty):
    if (tx-hx == 1 and ty-hy > 1) or (tx-hx > 1 and ty-hy == 1) or (tx-hx > 1 and ty-hy > 1):
        return -1,-1
    elif (tx-hx == -1 and ty-hy > 1) or (tx-hx < -1 and ty-hy == 1) or (tx-hx < -1 and ty-hy > 1):
        return 1,-1
    elif (tx-hx == 1 and ty-hy < -1) or (tx-hx > 1 and ty-hy == -1) or (tx-hx > 1 and ty-hy < -1):
        return -1,1
    elif (tx-hx == -1 and ty-hy < -1) or (tx-hx < -1 and ty-hy == -1) or (tx-hx < -1 and ty-hy < -1):
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

def part2():
    file = open('input.txt','r')
    tail = [[0,0,[]],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()],[0,0,set()]]
    for row in file:
        if "U" in row:
            for _ in range(int(row.split(" ")[1])):
                tail[0][1] += 1
                tail[0][2].append(str(tail[0][0])+" "+str(tail[0][1]))
                for i in range(1,len(tail)):
                    tmptx,tmpty = checkTail(tail[i-1][0],tail[i-1][1],tail[i][0],tail[i][1])
                    tail[i][0] += tmptx
                    tail[i][1] += tmpty
                    tail[i][2].add(str(tail[i][0])+" "+str(tail[i][1]))
        elif "D" in row:
            for _ in range(int(row.split(" ")[1])):
                tail[0][1] -= 1
                tail[0][2].append(str(tail[0][0])+" "+str(tail[0][1]))
                for i in range(1,len(tail)):
                    tmptx,tmpty = checkTail(tail[i-1][0],tail[i-1][1],tail[i][0],tail[i][1])
                    tail[i][0] += tmptx
                    tail[i][1] += tmpty
                    tail[i][2].add(str(tail[i][0])+" "+str(tail[i][1]))
        elif "L" in row:
            for _ in range(int(row.split(" ")[1])):
                tail[0][0] -= 1
                tail[0][2].append(str(tail[0][0])+" "+str(tail[0][1]))
                for i in range(1,len(tail)):
                    tmptx,tmpty = checkTail(tail[i-1][0],tail[i-1][1],tail[i][0],tail[i][1])
                    tail[i][0] += tmptx
                    tail[i][1] += tmpty
                    tail[i][2].add(str(tail[i][0])+" "+str(tail[i][1]))
        elif "R" in row:
            for _ in range(int(row.split(" ")[1])):
                tail[0][0] += 1
                tail[0][2].append(str(tail[0][0])+" "+str(tail[0][1]))
                for i in range(1,len(tail)):
                    tmptx,tmpty = checkTail(tail[i-1][0],tail[i-1][1],tail[i][0],tail[i][1])
                    tail[i][0] += tmptx
                    tail[i][1] += tmpty
                    tail[i][2].add(str(tail[i][0])+" "+str(tail[i][1]))
 
    print(len(tail[9][2]))

part2()