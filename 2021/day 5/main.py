def parse():
    data = []
    with open("./2021/day 5/input.txt", "r") as f:
        lines = f.read().split("\n")
        for i in lines:
            print(lines)
            start = i.split(" -> ")[0].split(",")
            end = i.split(" -> ")[1].split(",")
            data.append([int(start[0]), int(start[1]), int(end[0]), int(end[1])])
    return data

data = parse()

def part1(data):
    continue