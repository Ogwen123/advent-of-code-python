data = []
with open("./2023/2/input.txt", "r") as f:
    data = f.read().split("\n")

def part1():
    total = 0
    red_check = 12
    green_check = 13
    blue_check = 14
    for i in data:
        possible = True
        id = int(i.split(":")[0].split(" ")[-1])
        subsets = i.split(":")[-1].split(";")
        for j in subsets:
            red = 0
            green = 0
            blue = 0
            for k in j.split(","):
                if k.split(" ")[-1] == "blue":
                    blue = int(k.split(" ")[1])
                if k.split(" ")[-1] == "red":
                    red = int(k.split(" ")[1])
                if k.split(" ")[-1] == "green":
                    green = int(k.split(" ")[1])
            if red > red_check or green > green_check or blue > blue_check:
                possible = False
        if possible:
            total += id
    print(f"Part 1: {total}")
        
        
def part2():
    total = 0
    for i in data:
        id = int(i.split(":")[0].split(" ")[-1])
        subsets = i.split(":")[-1].split(";")
        big_red = 0
        big_green = 0
        big_blue = 0
        for j in subsets:
            red = 0
            green = 0
            blue = 0
            for k in j.split(","):
                if k.split(" ")[-1] == "blue":
                    blue = int(k.strip().split(" ")[0])
                elif k.split(" ")[-1] == "red":
                    red = int(k.strip().split(" ")[0])
                elif k.split(" ")[-1] == "green":
                    green = int(k.strip().split(" ")[0])
            if red > big_red: big_red = red
            if green > big_green: big_green = green
            if blue > big_blue: big_blue = blue
            
        total += big_red*big_green*big_blue
    print(f"Part 2: {total}")


part1()
part2()