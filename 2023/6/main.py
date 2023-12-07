data = []
with open("./2023/6/input.txt", "r") as f:
    data = f.read().split("\n")

def part1():
    times = data[0].split(":")[-1].strip().split(" "*5)
    distances = data[1].split(":")[-1].strip().split(" "*3)
    win_count = [0, 0, 0, 0]
    for i in range(len(times)):
        time = int(times[i])
        for j in range(time):
            if j*(time-j) > int(distances[i]):
                win_count[i] += 1
    total = 1
    for i in win_count:
        total *= i
    print(f"Part 1: {total}")

def part2():
    time = int(data[0].split(":")[-1].replace(" ", ""))
    distance = int(data[1].split(":")[-1].replace(" ", ""))
    total = 0
    for i in range(time):
        if i*(time-i) > distance:
            total += 1
    print(f"Part 2: {total}")

part1()
part2()