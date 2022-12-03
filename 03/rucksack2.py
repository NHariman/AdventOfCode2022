#!/usr/bin/python3

#Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
def stringcompare(s1, s2, s3):
	for i in s1:
		for j in s2:
			if (j == i):
				for k in s3:
					if (k == j):
						return k

def assign_priority(item):
	value = 0
	if (item.isupper() == True):
		value = ord(item[0]) - ord('A') + 27
	else:
		value = ord(item[0]) - ord('a') + 1
	return value

def find_common_item(group):
	common_item = stringcompare(group[0], group[1], group[2])
	priority = assign_priority(common_item)
	return priority

items = []
group = []

with open("03.txt", "r") as file:
	while True:
		for i in range(3):
			data = file.readline()
			if (len(data) == 0):
				break
			data = data.strip() # removes newline
			group.append(data)
		if not group:
			break 
		value = find_common_item(group)
		items.append(value)
		group = []
	file.close()

total = 0
for item in items:
	total += item

print(total)
