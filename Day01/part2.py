def part1():
    file = open('input.txt','r')
    output = [0]
    i = 0
    for row in file:
        if row == "\n":
            i += 1
            output.append(0)
        else:
            output[i] += int(row)
    print(sum(sorted(output, reverse=True)[:3]))

part1()