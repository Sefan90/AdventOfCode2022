import sympy

def rec(input,file):
    if input.isnumeric() or input == "x":
        return input
    else:
        output = "("
        for s in input.split(" "):
            if s in ["+","-","*","/","=","x"]:
                output += s
            else:
                output += rec(file[s],file)
        return output+")"

def part2():
    file = {r.split(":")[0]:r.split(":")[1].replace("\n","").strip() for r in open('input.txt','r')}
    tmp = rec(file["root"],file)
    x = sympy.symbols('x')
    y = sympy.sympify(tmp[1:-1].split("=")[0])
    z = sympy.sympify(str(eval(tmp[1:-1].split("=")[1])))
    print(sympy.solve(sympy.Eq(y,z),x))
 
part2()