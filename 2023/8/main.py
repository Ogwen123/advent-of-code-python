from math import gcd

def parse():
    data = {}
    with open("./2023/8/input.txt", "r") as f:
        split_file = f.read().split("\n\n")
        temp  = split_file[1].split("\n")
        dirs = split_file[0]
        for i in temp:
            data[i.split(" = ")[0]] = i.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")
        return data, dirs

data, directions = parse()

def part1():
    steps = 0
    current_pos = "AAA"
    dir_index = 0
    while True:
        steps += 1
        side = 0
        if directions[dir_index] == "L": side = 0
        else: side = 1
        current_pos = data[current_pos][side]
        if current_pos == "ZZZ":
            break
        dir_index = (dir_index + 1) % len(directions)
    print(f"Part 1: {steps}")

def part2():
    all_steps = []
    positions = []
    for i in data.keys():
        if i[-1] == "A":
            positions.append(i)
    for current_pos in positions:
        steps = 0
        dir_index = 0
        while True:
            steps += 1
            side = 0
            if directions[dir_index] == "L": side = 0
            else: side = 1
            current_pos = data[current_pos][side]
            if current_pos[-1] == "Z":
                break
            dir_index = (dir_index + 1) % len(directions)
        all_steps.append(steps)
    answer = 1
    for i in all_steps:
        answer = answer*i//gcd(answer, i)
    print(f"Part 2: {answer}")

part1()
part2()
