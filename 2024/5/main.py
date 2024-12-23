rules = []
orders = []
with open("./2024/5/input.txt", "r") as f:
    data = f.read().split("\n\n")
    orders = data[1].split("\n")
    for i in data[0].split("\n"): 
        rules.append([int(i.split("|")[0]), int(i.split("|")[1])])

def part1():
    answer = 0
    for i in orders:
        order = list(map(int, i.split(",")))
        for j in rules:
            if j[0] in order and j[1] in order and order.index(j[0]) > order.index(j[1]): break
        else: answer += order[len(order)//2]

    return answer

def part2():
    answer = 0
    for i in orders:
        order = list(map(int, i.split(",")))
        changed = False
        for _ in range(5):
            for j in rules:
                if j[0] in order and j[1] in order and order.index(j[0]) > order.index(j[1]):
                    changed = True
                    l1 = order.index(j[0])
                    l2 = order.index(j[1])

                    order[l1] = j[1]
                    order[l2] = j[0]
        if changed: answer += order[len(order)//2]

    return answer

print(part1())
print(part2())