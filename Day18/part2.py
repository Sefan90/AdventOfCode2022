def test(map3d,size,i,j,k):
    tmp_count = 6
    for a in range(0,i):
        if map3d[a][j][k] == 1:
            tmp_count -= 1
            break
    for a in range(i+1,size[0]):
        if map3d[a][j][k] == 1:
            tmp_count -= 1    
            break
    for a in range(0,j):
        if map3d[i][a][k] == 1:
            tmp_count -= 1
            break
    for a in range(j+1,size[1]):
        if map3d[j][a][k] == 1:
            tmp_count -= 1    
            break
    for a in range(0,k):
        if map3d[i][j][a] == 1:
            tmp_count -= 1
            break
    for a in range(j+1,size[2]):
        if map3d[i][j][a] == 1:
            tmp_count -= 1   
            break
    print(tmp_count)
    return tmp_count 


def part1():
    file = [[int(c) for c in r.replace("\n","").split(",")] for r in open('input.txt','r')]
    size = [0,0,0]
    for r in file:
        for i in range(len(r)):
            if r[i]+1 > size[i]:
                size[i] = r[i]+1
    print(file)
    print(size)
    map3d = []
    for i in range(size[0]):
        map3d.append([])
        for j in range(size[1]):
            map3d[i].append([])
            for k in range(size[2]):
                map3d[i][j].append([])
                if [i,j,k] in file:
                    map3d[i][j][k] = 1
                else:
                    map3d[i][j][k] = 0

    count = 0
    for i in range(size[0]):
        for j in range(size[1]):
            for k in range(size[2]):
                if map3d[i][j][k] == 1:
                    count += test(map3d,size,i,j,k)
    print(count)
    
part1()