def part2():
    file = open('input.txt','r')
    next = False
    stacks = [[],[],[],[],[],[],[],[],[]]
    for row in file:
        if row == "\n":
            next = True
        elif next == False:
            for i in range(0,len(row),4):
                for j in range(0,4):
                    if row[i+j] != " " and row[i+j] != "[" and row[i+j] != "]" and row[i+j] != "\n" and row[i+j] != "1" and row[i+j] != "2" and row[i+j] != "3":
                        stacks[int(i/4)].append(row[i+j])
        else:
            rowList= row.replace("\n","").split(" ")
            tmp=[]
            for _ in range(0,int(rowList[1])):
                tmp.append(stacks[int(rowList[3])-1].pop(0))
            for t in reversed(tmp):
                stacks[int(rowList[5])-1].insert(0,t)
        print(stacks)
    for s in stacks:
        print(s[0])
part2()