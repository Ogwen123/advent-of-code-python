rules = {}
orders = []
with open("./2024/5/input.txt", "r") as f:
    data = f.read().split("\n\n")
    orders = data[1].split("\n")
    rawRules = data[0].split("\n")
    for i in rawRules: 
        rules[int(i.split("|")[0])] = int(i.split("|")[1])

def part1():
    answer = 0
    for i in orders:
        order = list(map(int, i.split(",")))
        bad = []
        for j in range(len(order)):
            num = order[j]
            if num in rules and rules[num] in bad:
                break
            else:
                bad.append(num)
        else: answer += order[len(order)//2]
    return answer

print(part1())