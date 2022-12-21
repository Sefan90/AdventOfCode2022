def rec(input,file):
    if input.isnumeric():
        return input
    else:
        output = "("
        for s in input.split(" "):
            if s in ["+","-","*","/"]:
                output += s
            else:
                output += rec(file[s],file)
        return output+")"


def part1():
    file = {r.split(":")[0]:r.split(":")[1].replace("\n","").strip() for r in open('input.txt','r')}
    print(eval(rec(file["root"],file)))

    
part1()