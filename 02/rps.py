#!/usr/bin/python

# Opponent
# A = rock = 1
# B = paper = 2
# C = scissors = 3

# you
# X = rock = 1
# Y = paper = 2
# Z = scissors = 3

# scores
# win = 6
# lose = 0
# tie = 3

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
	if (choice == "A" or choice == "X"):
		return 1
	elif (choice == "B" or choice == "Y"):
		return 2
	elif (choice == "C" or choice == "Z"):
		return 3

def calculate_outcome(values):
	opponent = 0
	you = 0
	opponent = calc_choice(values[0])
	you = calc_choice(values[1])
	score = calc_score(opponent, you)
	return score + you

# reads file and totals up calories
with open("aoc_02.txt", "r") as file:
	while True:
		data = file.readline()
		if (len(data) == 0):
			break 
		values = data.strip() # removes newline
		split_values = values.split(' ') # splits into list based on space
		score_outcome = calculate_outcome(split_values) # calculates outcome
		split_values.append(score_outcome) # appends score outcome to values
		scores.append(split_values) # adds it to list for saving

#calculate total, totals victory total
total = 0
for score in scores:
	total += score[2]

print total
