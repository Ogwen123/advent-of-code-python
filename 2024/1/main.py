data = []
with open("./2024/1/input.txt", "r") as f:
    data = f.read().split("\n")

def split_pairs():
    l1 = []
    l2 = []
    
    for i in data:
        pair = i.split("   ")
        l1.append(int(pair[0]))
        l2.append(int(pair[1]))
    
    return l1, l2

def part1():
    answer = 0
    
    l1, l2 = split_pairs()
    
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    for i in range(len(l1)):
        answer += (max(l1[i], l2[i]) - min(l1[i], l2[i]))
    
    return answer

def part2():
    answer = 0
    
    l1, l2 = split_pairs()
    for i in l1:
        occurences = l2.count(i)
        answer += i * occurences
    
    return answer

print(part1())
print(part2())