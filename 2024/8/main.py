data = []
with open("./2024/8/input.txt", "r") as f:
    data = f.read().split("\n")
    
def part1():
    nodes = {}
    for rindex, i in enumerate(data):
        for cindex, j in enumerate(i):
            if j != ".":
                if j not in nodes:
                    nodes[j] = []
                nodes[j].append((rindex, cindex))
    
    count = 0
    
    locs = []
    
    for node, node_locs in nodes.items():
        for i in node_locs:
            for j in node_locs:
                if i == j: continue
                diff = (i[0] - j[0], i[1] - j[1])
                antinode = (j[0] - diff[0], j[1] - diff[1])
                locs.append((j[0] - diff[0], j[1] - diff[1]))
                
    loc = set(locs)
    
    answer = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in locs: answer += 1
    
    return answer

def part2():
    nodes = {}
    for rindex, i in enumerate(data):
        for cindex, j in enumerate(i):
            if j != ".":
                if j not in nodes:
                    nodes[j] = []
                nodes[j].append((rindex, cindex))
    
    count = 0
    
    locs = []
    
    for node, node_locs in nodes.items():
        for i in node_locs:
            for j in node_locs:
                if i == j: continue
                diff = (i[0] - j[0], i[1] - j[1])
                antinode = (j[0] - diff[0], j[1] - diff[1])
                for k in range(100):
                    locs.append((j[0] - diff[0]*k, j[1] - diff[1]*k))
                
    loc = set(locs)
    
    answer = 0
    for i in range(len(data)): # prune the locations to remove ones not in the bounds of the map
        for j in range(len(data[0])):
            if (i, j) in locs: answer += 1
    return answer

print(part1())
print(part2())
