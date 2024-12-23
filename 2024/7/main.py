import itertools

data = []
with open("./2024/7/input.txt", "r") as f:
    data = f.read().split("\n")

def do_maths(lst):
    numbuffer = lst[0]
    opbuffer = ""
    
    for i in lst[1:]:
        
        if type(i) is int:
            if opbuffer == "+": numbuffer += i
            elif opbuffer == "*": numbuffer *= i
            else: numbuffer = int(str(numbuffer) + str(i))
        else:
            opbuffer = i
    return numbuffer

def part1():
    answer = 0
    for i in data:
        val = int(i.split(": ")[0])
        vals = list(map(int, i.split(": ")[1].split(" ")))
        
        operators = list(itertools.product(["+", "*"], repeat=(len(vals) - 1)))
        for j in operators:
            buffer = [vals[0]]
            for index, k in enumerate(j):
                buffer.append(k)
                buffer.append(vals[index + 1])
            if do_maths(buffer) == val:
                answer += val
                break
    return answer

def part2():
    answer = 0
    for i in data:
        val = int(i.split(": ")[0])
        vals = list(map(int, i.split(": ")[1].split(" ")))
        
        operators = list(itertools.product(["+", "*", "||"], repeat=(len(vals) - 1)))
        for j in operators:
            buffer = [vals[0]]
            for index, k in enumerate(j):
                buffer.append(k)
                buffer.append(vals[index + 1])
            if do_maths(buffer) == val:
                answer += val
                break
    return answer

print(part1())
print(part2())