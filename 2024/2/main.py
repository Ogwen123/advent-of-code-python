data = []
with open("./2024/2/input.txt", "r") as f:
    data = f.read().split("\n")

def diff(x, y): return max(x, y) - min(x, y)

def check(i):
    values = list(map(int, i.split()))
    sort = sorted(values)
    
    asc = None
    if sort == values:
        asc = True
    elif sort == values[::-1]:
        asc = False
    else:
        return
    
    new_vals = [values[0]]
    for j in values[1:]:
        d = j - new_vals[-1] if asc else new_vals[-1] - j
        if 1 <= d <= 3:
            new_vals.append(j)
    if len(new_vals) == len(values): return True
    else: return False

def part1():
    answer = 0
    for i in data:
        if check(i) == True: answer += 1
        

    return answer



def part2():
    answer = 0
    for i in data:
        if check(i) == True: answer += 1
        else:
            for j in range(len(i)):
                prev_values = list(map(int, i.split()))
                values = prev_values[:j] + prev_values[j+1:]
                if check(" ".join(list(map(str, values)))):
                    answer += 1
                    break

    return answer

print(part1())
print(part2())