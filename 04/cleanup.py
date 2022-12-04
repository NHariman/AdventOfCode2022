def get_range(range_one, range_two):
	if not range_one:
		return False
	if not range_two:
		return False
	if ((range_one[0] >= range_two[0] and range_one[1] <= range_two[1]) or 
			(range_two[0] >= range_one[0] and range_two[1] <= range_one[1])):
		return True
	else:
		return False
	

def	compare_range(duo):
	split = duo.split(",")
	range_one = split[0].split("-")
	range_two = split[1].split("-")
	nbr_one = [ int(range_one[0]), int(range_one[1])]
	nbr_two = [ int(range_two[0]), int(range_two[1])]
	value = get_range(nbr_one, nbr_two)
	return value


amount = 0
with open("04.txt", "r") as file:
	while True:
		data = file.readline()
		data = data.strip()
		if (len(data) == 0):
			break 
		value = compare_range(data)
		if (value == True):
			amount += 1
	file.close()

print(amount)