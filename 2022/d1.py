import time
start = time.time()
with open("./Inputs/d1.txt", "r") as file:
    data = file.read()

split_data = data.split("\n")

print(split_data)

main_list = []

counter = 0

temp_list = []
for i in split_data:
    if not i == "":
        temp_list.append(i)
    else:
        main_list.append(temp_list)
        temp_list = []

highest = [0, 0, 0]

for i in range(len(main_list)):
    highest.sort(reverse=True)
    tracker = 0
    for j in main_list[i]:
        tracker += int(j)

    if tracker > highest[-1]:
        highest[-1] = tracker


print(highest[0] + highest[1] + highest[2])
print(time.time() - start)


