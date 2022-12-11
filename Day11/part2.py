def part2():
    file = open('input.txt','r')
    monkey = []
    current = -1
    for row in file:
        row = row.replace("\n","")
        if "Monkey" in row:
            monkey.append([0])
            current += 1
        elif "Starting items" in row:
            monkey[current].append([int(i) for i in row[18:].replace(",","").split(" ")])
        elif "Operation" in row:
            monkey[current].append(row.split("=")[1])
        elif "Test" in row:
            monkey[current].append(int(row.split(" ")[5]))
        elif "true" in row:
            monkey[current].append(int(row.split(" ")[9]))
        elif "false" in row:
            monkey[current].append(int(row.split(" ")[9]))

    for _ in range(10000):
        for item in monkey:
            for i in range(len(item[1])):
                item[0] += 1
                item[1][i] = eval(item[2].replace("old",str(item[1][i])))
                if item[1][i] % item[3] == 0:
                    monkey[item[4]][1].append(item[1][i])
                else:
                    monkey[item[5]][1].append(item[1][i])
            item[1] = []
    print(monkey)
    output = [0,0]
    for i in range(len(monkey)):
        if monkey[i][0] > output[0]:
            output[1] = output[0]
            output[0] = monkey[i][0]
        elif monkey[i][0] > output[1]:
            output[1] = monkey[i][0]
    print(output[0]*output[1])

part2()

#14398560027 low