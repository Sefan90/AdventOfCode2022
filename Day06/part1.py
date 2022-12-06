def part1():
    file = open('input.txt','r').readline()
    for i in range(4,len(file)+1):
        if file[i-4:i].count(file[i-1]) == 1 and file[i-4:i].count(file[i-2]) == 1 and file[i-4:i].count(file[i-3]) == 1 and file[i-4:i].count(file[i-4]) == 1:
            print(i)
            break

part1()