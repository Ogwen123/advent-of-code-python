data = []
with open("./2023/1/input.txt", "r") as f: data = f.read().split("\n")

def part1():
    total = 0
    for i in data:
        num_str = ""
        for letter in i:
            try: num_str += letter
            except: continue
        total += int(num_str[0] + num_str[-1])
    print(f"Part 1: {total}")

def part2():
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for i in data:
        num_str =""
        for j in range(len(i)):
            try:
                number = int(i[j])
                num_str += i[j]
            except:
                if i[j] in ["o", "t", "f", "s", "e", "n"]:
                    for k in numbers:
                        if i[j:j+len(k)] == k: num_str += str(numbers.index(k)+1)
        total += int(num_str[0] + num_str[-1])
    print(f"Part 2: {total}")

part1()
part2()