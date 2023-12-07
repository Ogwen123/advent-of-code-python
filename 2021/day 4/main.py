def part1(numbers, boards):
    last_value = 0

    for number in boards:
        for i in range(len(boards)):
            for j in range(len(boards[i])):
                for k in range(len(boards[j])):
                    if (number == boards[i][j][k]):
                        boards[i][j][k] == -1
                        last_value = number

if __name__ == "__main__":
    with open("./2021/day 4/input.txt", "r") as file:
        data = file.read().split("\n\n")
        numbers = data[0]
        card_strings = data[1:]#second item onwards
        boards = []
        for i in card_strings:
            print(i)
            print(".")
            line = i.split("\n")
            temp = []
            for i in line:
                temp2 = i.split(" ")
                for i in range(len(temp2)-5):
                    temp2.remove("")
                for i in range(len(temp2)):
                    temp2[i] = int(temp2[i])
                temp.append(temp2)
            boards.append(temp)
        print(boards)
        print("Part 1: " + str(part1(numbers, boards)))
