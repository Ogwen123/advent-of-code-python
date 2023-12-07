from collections import Counter

data = []
with open("./2023/7/input.txt", "r") as f:
    data = f.read().split("\n")

def is_stronger(one, two, cards): #  returns true if the first is stronger than the second
    one = one.split(" ")[0]
    two = two.split(" ")[0]
    for i in range(len(one)):
        if cards.index(one[i]) < cards.index(two[i]):
            return True
        elif cards.index(one[i]) > cards.index(two[i]):
            return False
        else:
            pass

def part1():
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    type_arr = {
        "fiveoak": [],
        "fouroak": [],
        "fullhouse": [],
        "threeoak": [],
        "twopair": [],
        "onepair": [],
        "highcard": []
    }
    for i in data:
        hand = i.split(" ")[0]
        bid = i.split(" ")[1]
        
        #find what type the hand is
        if len(hand) == len(set(list(hand))): type_arr["highcard"].append(i)
        elif len(hand)-1 == (len(set(list(hand)))): type_arr["onepair"].append(i)
        elif len(hand)-2 == (len(set(list(hand)))):
            count = Counter(hand).most_common()
            if count[0][1] == 3: type_arr["threeoak"].append(i)
            else: type_arr["twopair"].append(i)
        elif len(hand)-3 == (len(set(list(hand)))):
            count = Counter(hand).most_common()
            if count[0][1] == 4: type_arr["fouroak"].append(i)
            else: type_arr["fullhouse"].append(i)
        elif len(set(list(hand))) == 1: type_arr["fiveoak"].append(i)
        else:
            print(i)
            break
    
    #sort the type_arr into correct rank order
    types = ["fiveoak", "fouroak", "fullhouse", "threeoak", "twopair", "onepair", "highcard"]
    total_arr = []
    for t in types:
        arr = type_arr[t]
        for i in range(len(arr)): #  bubble sort
            for j in range(len(arr)-1):
                if is_stronger(arr[j+1], arr[j], cards):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        total_arr += arr
    
    length = len(total_arr)
    total = 0

    for i in range(length):
        bid = int(total_arr[i].split(" ")[1])
        rank = length-i
        total += bid*rank
        
    print(f"Part 1: {total}")
    
def part2():
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    type_arr = {
        "fiveoak": [],
        "fouroak": [],
        "fullhouse": [],
        "threeoak": [],
        "twopair": [],
        "onepair": [],
        "highcard": []
    }
    for i in data:
        hand = i.split(" ")[0]
        bid = i.split(" ")[1]
        
        # replace all the Js with the most common character
        freq = Counter(hand).most_common()
        
        replace_char = ""
        if freq[0][0] == "J" and len(freq) > 1:
            replace_char = freq[1][0]
        else:
            replace_char = freq[0][0]
        
        hand = hand.replace("J", replace_char)
        
        #find what type the hand is
        if len(hand) == len(set(list(hand))): type_arr["highcard"].append(i)
        elif len(hand)-1 == (len(set(list(hand)))): type_arr["onepair"].append(i)
        elif len(hand)-2 == (len(set(list(hand)))):
            count = Counter(hand).most_common()
            if count[0][1] == 3: type_arr["threeoak"].append(i)
            else: type_arr["twopair"].append(i)
        elif len(hand)-3 == (len(set(list(hand)))):
            count = Counter(hand).most_common()
            if count[0][1] == 4: type_arr["fouroak"].append(i)
            else: type_arr["fullhouse"].append(i)
        elif len(set(list(hand))) == 1: type_arr["fiveoak"].append(i)
        else:
            print(i)
            break
    
    #sort the type_arr into correct rank order
    types = ["fiveoak", "fouroak", "fullhouse", "threeoak", "twopair", "onepair", "highcard"]
    total_arr = []
    for t in types:
        arr = type_arr[t]
        for i in range(len(arr)): #  bubble sort
            for j in range(len(arr)-1):
                if is_stronger(arr[j+1], arr[j], cards):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        total_arr += arr
    
    length = len(total_arr)
    total = 0

    for i in range(length):
        bid = int(total_arr[i].split(" ")[1])
        rank = length-i
        total += bid*rank
        
    print(f"Part 2: {total}")

part1()
part2()