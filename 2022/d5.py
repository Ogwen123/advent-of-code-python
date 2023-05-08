from textwrap import wrap
import time
start = time.time()

with open("./Inputs/d5.txt", "r") as file:
    data = file.read()

temp_data = data.split("\n\n")

stack_data = temp_data[0]

data = temp_data[1]
data_list = data.split("\n")


def parse_move_commands(data_array):
    final_list = []
    for i in data_array:
        n1 = i.split(" ")[1]
        n2 = i.split(" ")[3]
        n3 = i.split(" ")[5]
        temp_list = [n1, n2, n3]
        final_list.append(temp_list)

    return final_list


data_list = parse_move_commands(data_list)


def do_rearrangement(data_array):
    stacks = [
        ["D", "T", "W", "F", "J", "S", "H", "N"],
        ["H", "R", "P", "Q", "T", "N", "B", "G"],
        ["L", "Q", "V"],
        ["N", "B", "S", "W", "R", "Q"],
        ["N", "D", "F", "T", "V", "M", "B"],
        ["M", "D", "B", "V", "H", "T", "R"],
        ["D", "B", "Q", "J"],
        ["D", "N", "J", "V", "R", "Z", "H", "Q"],
        ["B", "N", "H", "M", "S"]
    ]
    #probably incredibly inefficient but i cba to add a timer
    for i in data_array:
        quan = int(i[0])
        from_index = int(i[1])
        to_index = int(i[2])

        letters = stacks[from_index - 1][(len(stacks[from_index - 1]) - quan):]
        del stacks[from_index - 1][(len(stacks[from_index - 1]) - quan):]

        #print(letters)
        #letters.reverse()#uncomment for part 1

        for j in letters:
            stacks[to_index-1].append(j)

        #print(stacks)

    return stacks


stack_data = do_rearrangement(data_list)

string_list = []
for k in stack_data:
    string_list.append(k[-1])

string = str(string_list)
string = string.replace(",", "")
string = string.replace("[", "")
string = string.replace("]", "")
string = string.replace("'", "")
string = string.replace(" ", "")
print(string)
print(time.time() - start)

#NONE OF THIS FUCKING WORKS BECAUSE PYTHON REMOVES ALL THE TRAILING WHITESPACES FOR SOME FUCKING REASON SO IT COMPLETELY BREAKS THE INPUT
#def parse_stack_input(sd):
#    #string parsing
#    def list_to_string(s):
#        new = ""
#        for x in s:
#           new += x
#        return new
#
#    stacks = []
#    # sn=stack_num, sd = stack_data, sh = stack_height
#    sd = sd.split("\n")
#    sn = int(sd[-1][-1])  #saves the last number in the last string which is the string with the stack numbers to get how many stacks there are
#    sh = len(sd)
#    del sd[-1] #remove the stack numbers from the end
#
#    for i in range(sn):
#        stacks.append([])
#
#    print(sd)
#
#    for i in range(len(sd)):
#        temp_list = list(sd[i])
#        sd[i] = temp_list
#
#    print(sd)
#
#    for i in sd:
#        counter = 0
#        for j in range(len(i)):
#            if (j+1) % 4 == 0:
#                del i[j-counter]
#                counter += 1
#
#    print(sd)
#
#
#half_formatted_strings = []
#    for i in sd:
#        temp = i.replace("   ", "[-]")
#        #temp = temp.replace("[", "")
#        #temp = temp.replace("]", "")
#        half_formatted_strings.append(temp)
#
#    print(half_formatted_strings)
#
#    fully_formatted_strings = []
#    for i in half_formatted_strings:
#        temp_list = list(i)
#        counter = 0
#        for j in range(len(temp_list)-1):
#            if len(temp_list) == 9: break
#            if temp_list[j-counter] != " " and temp_list[j+1-counter] == " ":
#                del temp_list[j+1-counter] #remove the white spaces that are not a part of a stack and are just left over from the earlier parsing
#                counter += 1
#
#        fully_formatted_strings.append(list_to_string(temp_list))
#
#    print(fully_formatted_strings)
#
#    fully_formatted_strings.reverse()
#
#    print(fully_formatted_strings)
#
#    for i in range(sn):
#        for j in fully_formatted_strings:
#            stacks[i].append(j[i])
#
#    print(stacks)