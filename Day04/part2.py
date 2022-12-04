def part2():
    file = open('input.txt','r')
    same = 0
    for row in file:
        ids = [i.split("-") for i in row.replace("\n","").split(",")]
        if (int(ids[0][0]) >= int(ids[1][0]) and int(ids[0][0]) <= int(ids[1][1])):
            same += 1
        elif (int(ids[0][1]) >= int(ids[1][0]) and int(ids[0][1]) <= int(ids[1][1])):
            same += 1
        elif (int(ids[1][0]) >= int(ids[0][0]) and int(ids[1][0]) <= int(ids[0][1])):
            same += 1
        elif (int(ids[1][1]) >= int(ids[0][0]) and int(ids[1][1]) <= int(ids[0][1])):
            same += 1
    print(same)

part2()