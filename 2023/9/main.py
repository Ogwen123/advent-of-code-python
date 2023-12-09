from collections import Counter

data = []
with open("./2023/9/input.txt", "r") as f:
    data = f.read().split("\n")
    
def part1():
    total = 0
    for i in data:
        sequences = [[int(num) for num in i.split(" ")]]
        tracker = 0
        while True:
            next_seq = []
            cur_seq = sequences[-1]
            for j in range(len(cur_seq)-1):
                next_seq.append(cur_seq[j+1]-cur_seq[j])
            sequences.append(next_seq)
            check = Counter(next_seq).most_common()
            if check[0][1] == len(next_seq) and check[0][0] == 0: break

        for j in range(len(sequences)):
            tracker += sequences[j][-1]
        total += tracker
    print(f"Part 1: {total}")

def part2():
    total = 0
    for i in data:
        sequences = [[int(num) for num in i.split(" ")][::-1]]
        tracker = 0
        while True:
            next_seq = []
            cur_seq = sequences[-1]
            for j in range(len(cur_seq)-1):
                next_seq.append(cur_seq[j+1]-cur_seq[j])
            sequences.append(next_seq)
            check = Counter(next_seq).most_common()
            if check[0][1] == len(next_seq) and check[0][0] == 0: break

        for j in range(len(sequences)):
            tracker += sequences[j][-1]
        total += tracker
    print(f"Part 2: {total}")

part1()
part2()