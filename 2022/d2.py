import time
start = time.time()
scores = []

with open("./Inputs/d2.txt", "r") as file:
    data = file.read()

data_list = data.split("\n")

for i in data_list:
    opp = i[0]
    outcome = i[2]
    score = 0

    #A = rock
    #B = paper
    #C = scissors

    if outcome == "X":
        if opp == "A":
            score += 3

        if opp == "B":
            score += 1

        if opp == "C":
            score += 2

    if outcome == "Y":
        if opp == "A":
            score += 4

        if opp == "B":
            score += 5

        if opp == "C":
            score += 6

    if outcome == "Z":
        if opp == "A":
            score += 8

        if opp == "B":
            score += 9

        if opp == "C":
            score += 7

    scores.append(score)

final_score = 0
for i in scores:
    final_score += i

print(final_score)
print(time.time() - start)

#if you == "X" and opp == "A":
#    score += 4
#
#elif you == "X" and opp == "B":
#    score += 1
#
#elif you == "X" and opp == "C":
#    score += 7
#
#elif you == "Y" and opp == "B":
#    score += 5
#
#elif you == "Y" and opp == "C":
#    score += 2
#
#elif you == "Y" and opp == "A":
#    score += 8
#
#elif you == "Z" and opp == "C":
#    score += 6
#
#elif you == "Z" and opp == "A":
#    score += 3
#
#elif you == "Z" and opp == "B":
#    score += 9
#

