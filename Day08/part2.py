def checkTrees(file,r,c):
    tmpScore = 1
    for i in range(r-1,-1,-1):
        if file[r][c] <= file[i][c]:
            tmpScore *= r-i
            break
        elif i == 0:
            tmpScore *= r
    for i in range(c-1,-1,-1):
        if file[r][c] <= file[r][i]:
            tmpScore *= c-i
            break
        elif i == 0:
            tmpScore *= c
    for i in range(r+1,len(file)):
        if file[r][c] <= file[i][c]:
            tmpScore *= i-r
            break
        elif i == len(file)-1:
            tmpScore *= i-r
    for i in range(c+1,len(file[r])):
        if file[r][c] <= file[r][i]:
            tmpScore *= i-c
            break
        elif i == len(file[r])-1:
            tmpScore *= i-c
    return tmpScore
    

def part2():
    file = [[int(c) for c in r.replace("\n","")] for r in open('input.txt','r').readlines()]
    score = [[0 for c in r] for r in file]
    for r in range(len(file)):
        for c in range(len(file[r])):
            if r == 0 or c == 0 or r == len(file)-1 or c == len(file[r])-1:
                score[r][c] = 0
            else:
                score[r][c] = checkTrees(file,r,c)

    flatScore = [i for l in score for i in l]
    print(max(flatScore))
part2()
