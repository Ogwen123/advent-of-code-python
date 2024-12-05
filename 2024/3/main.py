import re

data = ""
with open("./2024/3/input.txt", "r") as f:
    data = f.read()

def parse_multiplication(string):
    nums = string[4:-1]
    numbers = nums.split(",")
    return int(numbers[0]) * int(numbers[1])

def part1():
    answer = 0
    count = 0
    while count < len(data):
        found = False
        for i in range(5):
            if re.search("^mul\(\d{1,3},\d{1,3}\)$", data[count:count + 8 + i]):
                answer += parse_multiplication(data[count:count + 8 + i])
                found = True
                count += (i + 1)
                break
        if found == False: count += 1
    
    return answer

def part2():
    answer = 0
    count = 0
    do = True
    while count < len(data):
        
        if data[count:count+4] == "do()": 
            do = True
            count += 4
            continue
        
        if data [count:count+7] == "don't()":
            do = False
            count += 7
            continue
        
        found = False
        if do:
            for i in range(5):
                if re.search("^mul\(\d{1,3},\d{1,3}\)$", data[count:count + 8 + i]):
                    answer += parse_multiplication(data[count:count + 8 + i])
                    found = True
                    count += (i + 1)
                    break
        if found == False: count += 1
    
    return answer

print(part1())
print(part2())