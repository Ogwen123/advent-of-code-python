import time
start = time.time()
with open("./Inputs/d4.txt", "r") as file:
    data  = file.read()

data_list = data.split("\n")

total_pairs = len(data_list)

def split_and_parse_pairs(data_list):
    final_list = []
    for i in data_list:
        tl1 = i.split(",")
        tl2 = []
        for j in tl1:
            #converts a range of numbers (e.g. 1-5) into a list of numbers (e.g. 1, 2, 3, 4, 5)
            a, b = j.split('-')
            a, b = int(a), int(b)
            result = range(a, b + 1)
            result = list(result)
            tl2.append(result)
        final_list.append(tl2)

    return final_list

data_list = split_and_parse_pairs(data_list)

#part 2
def find_any_overlap(data_list):
    overlaps = 0

    for i in data_list:
        l1 = i[0]
        l2 = i[1]

        for j in l1:
            if j in l2:
                overlaps += 1
                break

    return overlaps

print(find_any_overlap(data_list))

#part 1
def find_complete_overlaps(data_list):
    overlaps = total_pairs
    for i in data_list:
        l1 = i[0]
        l2 = i[1]
        #print(l1)
        #print(l2)
        overlap_tracker = [True, True]

        #if the first pair has any numbers not in the second pair or the second pair has any numbers
        #not in the first pair then they can be overlaps, so we subtract that from the total number of
        #pairs and at the end we are left with the number of completely overlapping pairs
        for j in l1:
            if j not in l2:#list just splits a string into a list of chars
                overlap_tracker[0] = False

        for j in l2:
            if j not in l1:
                overlap_tracker[1] = False

        if not overlap_tracker[0] and not overlap_tracker[1]:
            overlaps -= 1

    return overlaps

print(time.time() - start)

#print(find_complete_overlaps(data_list))
