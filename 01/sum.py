#!/usr/bin/python

file_path = 'aoc_01.txt'

calories_total = []

calories = 0

# reads file and totals up calories
with open(file_path, "r") as file:
	while True:
		data = file.readline()
		if (len(data) == 0):
			break 
		value = data.strip()
		if (len(value) == 0):
			calories_total.append(calories)
			calories = 0
		else:
			calories = calories + int(value)

#sorts calorie totals from highest to lowest
calories_total.sort(reverse=True)
print calories_total

#gets total of highest 3 calories
highest_calories = calories_total[0] + calories_total[1] + calories_total[2]
print highest_calories

file.close()
