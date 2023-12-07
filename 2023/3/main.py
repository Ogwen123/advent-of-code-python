data = []
with open("./2023/3/input.txt", "r") as f:
    data = f.read().split("\n")

def is_symbol(char):
    if not char.isnumeric() and not char == ".":
        return True
    return False
    
def part1():
    total = 0
    i = 0
    num_start = []
    num_len = 0
    while i < len(data):
        j = 0
        while j < len(data[i]):
            if data[i][j].isnumeric():
                num_len = 0
                temp = j
                num_start = [i, j]
                while temp <= len(data[i])-1 and data[i][temp].isnumeric():
                    num_len += 1
                    temp += 1
                    
                is_part = False
                # check front for symbol
                try:
                    if is_symbol(data[i-1][j-1]):
                        is_part = True
                except IndexError: pass
                try:
                    if is_symbol(data[i][j-1]):
                        is_part = True
                except IndexError: pass
                try:
                    if is_symbol(data[i+1][j-1]):
                        is_part = True
                except IndexError: pass
                
                # check top and bottom
                for k in range(num_len):
                    if i > 0 and is_symbol(data[i-1][j+k]):
                        is_part = True
                    elif i < len(data)-1 and is_symbol(data[i+1][j+k]):
                        is_part = True
                        
                try:
                    if is_symbol(data[i-1][j+num_len]): is_part = True
                except IndexError: pass
                try:
                    if is_symbol(data[i][j+num_len]): is_part = True
                except IndexError: pass
                try:
                    if is_symbol(data[i+1][j+num_len]): is_part = True
                except IndexError: pass
                
                if is_part:
                    num_str = ""
                    for k in range(num_len):
                        num_str += data[i][j+k]
                    total += int(num_str)
                j += num_len
            else:
                j += 1
                    
        i += 1
    print(f"Part 1: {total}")

def get_number(data, i, j):# get the full number give a digit somewhere in the number
    ti = i
    tj = j
    num_start_i = i
    num_start_j = 0
    num_str = ""
    while True:
        if not data[i][j].isnumeric() or j < 0:
            num_start_j = j + 1
            break
        j -= 1
        
    while num_start_j < len(data[i]):
        if not data[num_start_i][num_start_j].isnumeric(): break
        num_str += data[num_start_i][num_start_j]
        num_start_j += 1
    return int(num_str)

def part2():
    total = 0
    i = 0
    num_start = []
    num_len = 0
    while i < len(data):
        j = 0
        while j < len(data[i]):
            if data[i][j] == "*":
                nums = []
                
                try:
                    if data[i-1][j-1].isnumeric(): nums.append(get_number(data, i-1, j-1))
                except IndexError: pass
                try: 
                    if data[i-1][j].isnumeric(): nums.append(get_number(data, i-1, j))
                except IndexError: pass
                try: 
                    if data[i-1][j+1].isnumeric(): nums.append(get_number(data, i-1, j+1))
                except IndexError: pass
                try: 
                    if data[i][j-1].isnumeric(): nums.append(get_number(data, i, j-1))
                except IndexError: pass
                try: 
                    if data[i][j+1].isnumeric(): nums.append(get_number(data, i, j+1))
                except IndexError: pass
                try: 
                    if data[i+1][j-1].isnumeric(): nums.append(get_number(data, i+1, j-1))
                except IndexError: pass
                try: 
                    if data[i+1][j].isnumeric(): nums.append(get_number(data, i+1, j))
                except IndexError: pass
                try: 
                    if data[i+1][j+1].isnumeric(): nums.append(get_number(data, i+1, j+1))
                except IndexError: pass
                
                s_nums = set(nums)
                if len(s_nums) == 2:
                    total += list(s_nums)[0]*list(s_nums)[1]
                j += 1
            else:
                j += 1
                    
        i += 1
    print(f"Part 2: {total}")

part1()
part2()