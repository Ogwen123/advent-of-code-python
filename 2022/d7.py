with open("./Inputs/d7.txt", "r") as file:
    data = file.read()

data_list = data.split("\n")

def parse_data_into_list(data_list):
    for i in data_list:
        if i == "$ cd ..":
            return

OutputList = []
with open("./Inputs/d7.txt", "r") as data:
    for t in data:
        Line = t.strip()
        LineList = Line.split()
        LineTuple = tuple(LineList)
        OutputList.append(LineTuple)

print(OutputList)
