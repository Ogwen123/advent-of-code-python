data = []
with open("./2024/6/input.txt", "r") as f:
    data = [list(x) for x in f.read().split("\n")] 

def turn(d):
    if d == (0, -1): return (1, 0)
    if d == (1, 0): return (0, 1)
    if d == (0, 1): return (-1, 0)
    if d == (-1, 0): return (0, -1)

def icon(d):
    if d == (0, -1): return "^"
    if d == (1, 0): return ">"
    if d == (0, 1): return "v"
    if d == (-1, 0): return "<"

def part1():
    x = 0
    y = 0
    d = (0, -1)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "^": 
                x = j
                y = i
                break
            
    count = 0
    while True:
        if x > len(data[0]) - 1 or y > len(data) - 1 or x < 0 or y < 0: break
        count += 1
        infront = ""
        
        try: infront = data[y + d[1]][x + d[0]]
        except: infront = "."
        
        if infront == "#":
            d = turn(d)
            
        data[y][x] = "X"
        x, y = x + d[0], y + d[1]
        data[y][x] = icon(d)
        
        if count == 6000:
                #answer = 0
                #for i in range(len(data)):
                #    for j in range(len(data[i])):
                #        if data[i][j] == "X": answer += 1
                #print(answer)
                for i in data: 
                    try:
                        print("".join(i))
                    except: print(i)
    answer = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X": answer += 1
    
    return answer

print(part1())