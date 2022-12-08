def checkTrees(file,r,c):
    test = False
    for i in range(0,r):
        if file[r][c] <= file[i][c]:
            test = True
    if test == False:
        return 1
    test = False   
    for i in range(0,c):
        if file[r][c] <= file[r][i]:
            test = True
    if test == False:
        return 1
    test = False  
    for i in range(r+1,len(file)):
        if file[r][c] <= file[i][c]:
            test = True
    if test == False:
        return 1
    test = False  
    for i in range(c+1,len(file[r])):
        if file[r][c] <= file[r][i]:
            test = True
    if test == False:
        return 1
    return 0
    

def part1():
    file = [[int(c) for c in r.replace("\n","")] for r in open('input.txt','r').readlines()]
    visible = 0
    for r in range(len(file)):
        for c in range(len(file[r])):
            if r == 0 or c == 0 or r == len(file)-1 or c == len(file[r])-1:
                visible += 1
            else:
                visible += checkTrees(file,r,c)
    print(visible)
part1()
