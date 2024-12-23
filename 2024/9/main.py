data = []
with open("./2024/9/input.txt", "r") as f:
    data = list(f.read())

def part1():
    fs = []
    on_file = True
    count = 0
    empty_locs = []
    for i in data:
        if on_file:
            fs += list(str(count) * int(i))
            count += 1
            on_file = False
        else:
            empty_locs += list(map(lambda x: x + len(fs), list(range(int(i)))))
            fs += list("." * int(i))
            on_file = True
    empty_locs.reverse()

    for i in range(len(fs) - 1, 0, -1):
        if fs[i] != ".":
            j = empty_locs.pop()
            empty_locs.insert(0, i)
            if fs[j] == "." and j < i:
                temp = fs[j]
                fs[j] = fs[i]
                fs[i] = temp
    
    answer = 0
    for i in range(len(fs)):
        if fs[i] == ".": break
        answer += int(fs[i]) * i

    return answer
print(part1())