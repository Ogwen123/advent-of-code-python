import time
start = time.time()
with open("./Inputs/d3.txt", "r") as file:
    data  = file.read()

data_list = data.split("\n")

letters = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#part 2
def split_groups(data_list):
    group_list = []
    for i in range(len(data_list)//3):
        index = i*3
        temp_list = [data_list[index], data_list[index+1], data_list[index+2]]
        group_list.append(temp_list)
    return group_list

data_list = split_groups(data_list)

def find_badge_letter(data_list):
    counter = 0
    for i in data_list:
        s1 = i[0]
        s2 = i[1]
        s3 = i[2]

        for j in s1:
            if j in list(s2) and j in list(s3):
                counter += letters.index(j)
                break

    return counter

print(find_badge_letter(data_list))
print(time.time() - start)

#part 1
def find_common_letter():
    counter = 0
    for i in data_list:
        mid_point = (len(i))//2
        string1 = i[:mid_point]
        string2 = i[mid_point:]

        for j in string1:
            if j in list(string2):
                counter += letters.index(j)
                break

    return counter

#print(find_common_letter())