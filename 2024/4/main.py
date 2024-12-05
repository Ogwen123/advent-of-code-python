data = []
with open("./2024/4/input.txt", "r") as f:
    data = f.read().split("\n")

def part1():
    answer = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            letter = data[i][j]
            if letter != "X": continue
            try:
                if i - 3 < 0: data[1000000000000000000]
                if data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if i - 3 < 0: data[1000000000000000000]
                if data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if j - 3 < 0: data[1000000000000000000]
                if data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if j - 3 < 0: data[1000000000000000000]
                if data[i][j] + data[i][j-1] + data[i][j-2] + data[i][j-3] == "XMAS": answer += 1
            except IndexError: pass
            
            try:
                if i - 3 < 0 or j - 3 < 0: data[1000000000000000000]
                if data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3] == "XMAS": answer += 1
            except IndexError: pass
    return answer

def part2():
    answer = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            letter = data[i][j]
            if letter != "A": continue
            try:
                tl = data[i-1][j-1]
                bl = data[i+1][j-1]
                tr = data[i-1][j+1]
                br = data[i+1][j+1]
                
                if tl + br in ["MS", "SM"] and tr + bl in ["MS", "SM"]: answer += 1
            except IndexError: pass
            
    return answer

print(part1())
print(part2())