#!/usr/bin/python3

#Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
def stringcompare(sac_one, sac_two):
	for i in sac_one:
		for j in sac_two:
			if (j == i):
				return i

def assign_priority(item):
	value = 0
	if (item.isupper() == True):
		value = ord(item[0]) - ord('A') + 27
	else:
		value = ord(item[0]) - ord('a') + 1
	return value

def find_common_item(items_unsorted):
	length = len(items_unsorted)
	half_len = length/2
	sac_one = items_unsorted[0:int(half_len)]
	sac_two = items_unsorted[int(half_len):length]
	common_item = stringcompare(sac_one, sac_two)
	priority = assign_priority(common_item)
	return priority

items = []

with open("03.txt", "r") as file:
	while True:
		data = file.readline()
		if (len(data) == 0):
			break 
		items_unsorted = data.strip() # removes newline
		value = find_common_item(items_unsorted)
		items.append(value)
	file.close()

total = 0
for item in items:
	total += item

print(total)
