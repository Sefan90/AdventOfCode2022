def lookInDir0(d,path):
    size = 0
    for k, v in sorted(path.items(), key=len, reverse=True):
        if k.startswith(d):
            for i in v:
                if "dir" not in i:
                    size += int(i.split(" ")[0])
                    #print(d,k)
    return size

def lookInDir(d,path,dirSize):
    size = 0
    for i in path[d]:
        if "dir" not in i:
            size += int(i.split(" ")[0])
        else:
            print(d+i.split(" ")[1]+"-") 
            size += dirSize[d+i.split(" ")[1]+"-"]

    return size


def part1():
    file = open('input.txt','r')
    path = {"/-":['0 0']}
    currentdir = ""
    for row in file:
        if "$ cd" in row:
            if row.split(" ")[2] == "..\n":
                currentdir = currentdir[:currentdir.rfind("-",0,-1)+1]
            else:
                currentdir += row.replace("\n","").split(" ")[2]+"-"
                if currentdir not in path.keys():
                    path[currentdir] = []
        elif "dir" in row:
            path[currentdir] += [row.replace("\n","")]
            if currentdir+row.replace("\n","").split(" ")[1]+"-" not in path.keys():
                    path[currentdir+row.replace("\n","").split(" ")[1]+"-"] = []
        elif "$" not in row:
            path[currentdir].append(row.replace("\n",""))

    dirSize = {}
    print(path.keys()) 
    for d in sorted(path.keys(), key=len, reverse=True):
        if d not in dirSize.keys():
            dirSize[d] = 0
        dirSize[d] += lookInDir(d,path,dirSize)
    
    print(dirSize)
    print(sum([v for v in dirSize.values() if v <= 100000]))

part1()