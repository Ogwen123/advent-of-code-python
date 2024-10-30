data = []
with open("./2023/10/input.txt", "r") as f:
    data = f.read().split("\n")
    
move_combos  = {
    "| N": "N",
    "| S": "S",
    "- E": "E",
    "- W": "W",
    "L S": "E",
    "L W": "N",
    "J E": "N",
    "J S": "W",
    "7 N": "W",
    "7 E": "S",
    "F W": "S",
    "F N": "E",
}

def find_correct_start(y, x):
    # find correct starting place and direction
    try: return [y-1, x], move_combos[data[y-1][x]+" N"]
    except KeyError: pass
    
    try: return [y+1, x], move_combos[data[y+1][x]+" S"]
    except KeyError: pass
    
    try: return [y, x-1], move_combos[data[y][x-1]+" W"]
    except KeyError: pass
    
    try: return [y, x+1], move_combos[data[y][x+1]+" E"]
    except KeyError: pass
    
    return 

def part1():
    length = 1
    dir = "S" # N, E, S, W
    pos = [0, 0]
    # get the total length of the loop and half it i think
    for i, v1 in enumerate(data):
        for j, v2 in enumerate(v1):
            if v2 == "S": 
                pos, dir = find_correct_start(i, j)
    while True:
        if data[pos[0]][pos[1]] == "S":
            break
        match dir:
            case "N":
                pos = [pos[0]-1, pos[1]]
            case "E":
                pos = [pos[0], pos[1]+1]
            case "S":
                pos = [pos[0]+1, pos[1]]
            case "W":
                pos = [pos[0], pos[1]-1]
            case _:
                print("uhh ohh")
                break
        if data[pos[0]][pos[1]] == "S":
            length += 1
            break
        dir = move_combos[f"{data[pos[0]][pos[1]]} {dir}"]
        length += 1
        
    print(f"Part 1: {round(length/2)}")
    
part1()