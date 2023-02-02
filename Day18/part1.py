def part1():
    file = [[int(c) for c in r.replace("\n","").split(",")] for r in open('input.txt','r')]
    size = [0,0,0]
    for r in file:
        for i in range(len(r)):
            if r[i]+1 > size[i]:
                size[i] = r[i]+1
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
                    tmp_count = 6
                    for l in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
                        if (i+l[0]) < size[0] and (j+l[1]) < size[1] and (k+l[2]) < size[2]:
                            if map3d[i+l[0]][j+l[1]][k+l[2]] == 1:
                                tmp_count -= 1
                    count += tmp_count
    print(count)
    
part1()