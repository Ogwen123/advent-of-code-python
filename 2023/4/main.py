data = []
with open("./2023/4/input.txt", "r") as f:
    data = f.read().split("\n")

def part1():
    total = 0
    for i in data:
        count = 0
        good_data = i.split(":")[-1].strip()
        card = good_data.split("|")[0].strip().split(" ")
        my_nums = good_data.split("|")[-1].strip()
        for j in my_nums.split(" "):
            if j == "": continue
            if j in card:
                if count == 0:
                    count = 1
                else:
                    count = 2*count
        total += count
    print(f"Part 1: {total}")

def count_cards(card_list):
    for i in data:
        count = 0
        good_data = i.split(":")[-1].strip()
        card = good_data.split("|")[0].strip().split(" ")
        my_nums = good_data.split("|")[-1].strip()
        for j in my_nums.split(" "):
            if j == "": continue
            if j in card:
                if count == 0:
                    count = 1
                else:
                    count = 2*count
        total += count

def part2():
    total = 0
    for i in data:
        count = 0
        good_data = i.split(":")[-1].strip()
        card = good_data.split("|")[0].strip().split(" ")
        my_nums = good_data.split("|")[-1].strip()
        for j in my_nums.split(" "):
            if j == "": continue
            if j in card:
                if count == 0:
                    count = 1
                else:
                    count = 2*count
        total += count
    print(total)

part1()