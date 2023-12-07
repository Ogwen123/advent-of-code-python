import math

def parse():
    data = {}
    with open("./2023/5/input.txt", "r") as f:
        temp = f.read().split("\n\n")
        data["seeds"] = temp[0].split(":")[1].strip().split(" ")
        mapping_names = ["seedsoil", "soilfertilizer", "fertilizerwater", "waterlight", "lighttemp", "temphumidity", "humiditylocation"]
        for i, name in enumerate(mapping_names):
            data[name] = temp[i+1].split("\n")[1:]
    return data

data = parse()

def get_correct_mapping(code, mappings_name):
    mappings = data[mappings_name]
    for i in mappings:
        start = int(i.split(" ")[1])
        length = int(i.split(" ")[2])
        if start <= code <= start+length:
            return i
    return False

def part1():
    lowest = math.inf
    for i in data["seeds"]:
        codes = [int(i)]
        for j in data.keys():
            if j == "seeds": continue
            # get soil code
            mapping = get_correct_mapping(codes[-1], j)
            if mapping == False:
                codes.append(codes[-1])
            else:
                start_one = int(mapping.split(" ")[1])
                start_two = int(mapping.split(" ")[0])
                length = int(mapping.split(" ")[2])
                codes.append(start_two + (codes[-1]-start_one))
        if codes[-1] < lowest:
            lowest = codes[-1]
    
    print(f"Part 1: {lowest}")

def part2():
    lowest = math.inf
    count = 0
    while count <= len(data["seeds"])//2:
        seeds = range(int(data["seeds"][count]), int(data["seeds"][count])+int(data["seeds"][count+1]))
        for i in data["seeds"]:
            codes = [int(i)]
            for j in data.keys():
                if j == "seeds": continue
                # get soil code
                mapping = get_correct_mapping(codes[-1], j)
                if mapping == False:
                    codes.append(codes[-1])
                else:
                    start_one = int(mapping.split(" ")[1])
                    start_two = int(mapping.split(" ")[0])
                    length = int(mapping.split(" ")[2])
                    codes.append(start_two + (codes[-1]-start_one))
            if codes[-1] < lowest:
                lowest = codes[-1]
    
    print(f"Part 2: {lowest}")

part1()
part2()