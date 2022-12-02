#!/usr/bin/python

# Opponent
# A = rock = 1
# B = paper = 2
# C = scissors = 3

# you
# X = lose = 0
# Y = draw = 3
# Z = win = 6

scores = []

def calc_score(opponent, you):
	if (opponent == you):
		return 3
	elif (opponent == 1 and you == 2 or 
			opponent == 2 and you == 3 or
			opponent == 3 and you == 1):
		return 6
	else:
		return 0

def calc_choice(choice):
	if (choice == "A"):
		return 1
	elif (choice == "B"):
		return 2
	elif (choice == "C"):
		return 3

def calc_move(outcome, opponent):
	if (outcome == "Y"):
		return opponent
	elif (outcome == "Z"):
		if (opponent == 3):
			return 1
		else:
			return opponent + 1
	elif (outcome == "X"):
		if (opponent == 1):
			return 3
		else:
			return opponent - 1

def calculate_outcome(values):
	opponent = 0
	you = 0
	opponent = calc_choice(values[0])
	you = calc_move(values[1], opponent)
	score = calc_score(opponent, you)
	return score + you

# reads file and totals up calories
with open("aoc_02.txt", "r") as file:
	while True:
		data = file.readline()
		if (len(data) == 0):
			break 
		values = data.strip()
		split_values = values.split(' ')
		score_outcome = calculate_outcome(split_values)
		split_values.append(score_outcome)
		scores.append(split_values)

total = 0
for score in scores:
	total += score[2]

print total
