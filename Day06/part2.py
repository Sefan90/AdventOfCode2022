def part2():
    file = open('input.txt','r').readline()
    for i in range(14,len(file)+1):
        test = True
        for j in range(1,15):
            if file[i-14:i].count(file[i-j]) != 1:
                test = False
                break
        if test == True:
            print(i)
            break
        
part2()