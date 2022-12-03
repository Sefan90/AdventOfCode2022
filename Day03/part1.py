def toNumber(char):
    char = ord(char)
    if char < 91:
        return char-38
    else:
        return char-96

def part1():
    file = open('input.txt','r')
    types = 0
    for row in file:
        item1 = row[:int(len(row)/2)]
        item2 = row[int(len(row)/2):]
        for c in item1:
            if c in item2:
                types += toNumber(c)
                break
    print(types)

part1()