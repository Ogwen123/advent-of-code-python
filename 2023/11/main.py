import time

data = []
with open("./2023/11/input.txt", "r") as f:
    data = f.read().split("\n")

def part1():
    #expand the galaxy
    expand_rows = []
    expand_cols = []

    #rows
    for i in range(len(data)):
        clear = True
        for j in range(len(data[i])):
            if data[i][j] == "#":
                clear = False
                break
        if clear: expand_rows.append(i)

    # cols
    for i in range(len(data[0])):
        j = 0
        clear = True
        while j < len(data):
            if data[j][i] == "#":
                clear = False
                break
            j += 1
        if clear:
            expand_cols.append(i)
    
    count = 0
    for i in expand_rows:
        data.insert(i+count, "."*len(data[i]))
        count += 1
    
    for i in range(len(data)):
        d = list(data[i])
        count = 0
        for j in expand_cols:
            d.insert(j+count, ".")
            count += 1
        data[i] = "".join(d)
        
    # find shortest paths
    total = 0
    gal_locs = []
    done_pairs = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                gal_locs.append([i, j])
    
    count = 0
    for i1 in gal_locs:
        for i2 in range(count, len(gal_locs)):
            i = i1[0]
            j = i1[1]
            k = gal_locs[i2][0]
            h = gal_locs[i2][1]
            s = ""
            if i1 == i2: continue
            if i == k:
                if min(j, h) == j: s = f"{i}-{j}|{k}-{h}"
                else: s = f"{k}-{h}|{i}-{j}"
            else:
                if min(i, k) == i: s = f"{i}-{j}|{k}-{h}"
                else: s = f"{k}-{h}|{i}-{j}"
            
            if not s in done_pairs:
                total += abs((i-k)) + abs((j-h))
                done_pairs.append(s)
        count += 1
    print(f"Part 1: {total}")

def get_list_pos(num, arr):
    index = 0
    biggest_less_than = 0
    for i in range(len(arr)):
        if arr[i] < num:
            biggest_less_than = arr[i]
            index = i
    return index

def part2():
    total = 0
    mutliplier = 1_000_000-1
    #expand the galaxy
    expand_rows = [0]
    expand_cols = [0]

    #rows
    for i in range(len(data)):
        clear = True
        for j in range(len(data[i])):
            if data[i][j] == "#":
                clear = False
                break
        if clear: expand_rows.append(i)

    # cols
    for i in range(len(data[0])):
        j = 0
        clear = True
        while j < len(data):
            if data[j][i] == "#":
                clear = False
                break
            j += 1
        if clear:
            expand_cols.append(i)
            
    gal_locs = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                gal_locs.append([i, j])
    
    for i in range(len(gal_locs)):
        loc = gal_locs[i]

        loc[0] = loc[0] + mutliplier*get_list_pos(loc[0], expand_rows)
        loc[1] = loc[1] + mutliplier*get_list_pos(loc[1], expand_cols)

    count = 0
    done_pairs = []
    for i1 in gal_locs:
        for i2 in range(count, len(gal_locs)):
            i = i1[0]
            j = i1[1]
            k = gal_locs[i2][0]
            h = gal_locs[i2][1]
            s = ""
            if i1 == i2: continue
            if i == k:
                if min(j, h) == j: s = f"{i}-{j}|{k}-{h}"
                else: s = f"{k}-{h}|{i}-{j}"
            else:
                if min(i, k) == i: s = f"{i}-{j}|{k}-{h}"
                else: s = f"{k}-{h}|{i}-{j}"
            
            if not s in done_pairs:
                total += abs((i-k)) + abs((j-h))
                done_pairs.append(s)
        count += 1
    print(f"Part 2: {total}")
    
#part1()
part2()