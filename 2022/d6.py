import time
start = time.time()

with open("./Inputs/d6.txt", "r") as file:
    data = file.read()

data_list = list(data)

def find_marker(data_array, MARKER_LENGTH):
    for i in range(len(data_array)-MARKER_LENGTH):
        letter_block = data_array[i:i+MARKER_LENGTH]
        if len(letter_block) == len(set(letter_block)):
            return i+MARKER_LENGTH


print(f"Part 1: {str(find_marker(data_list, 4))}")
print(f"Part 2: {str(find_marker(data_list, 14))}")

print(time.time() - start)