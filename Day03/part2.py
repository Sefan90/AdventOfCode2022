def toNumber(char):
    char = ord(char)
    if char < 91:
        return char-38
    else:
        return char-96

def part2():
    file = [row for row in open('input.txt','r')]
    types = 0
    for i in range(0,len(file),3):
        for c in file[i]:
            if c in file[i+1] and c in file[i+2]:
                types += toNumber(c)
                break
    print(types)

part2()