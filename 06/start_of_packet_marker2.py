# read in data

# checks every packet if all are unique
def is_unique(packet):
	for i in range(14):
		for j in range(i + 1, 14):
			if (packet[j] == packet[i]):
				return False
	return True

file_obj = open("06.txt", "r")
data = file_obj.readlines()
data = data[0].strip() # removes newline

# reads until 4 charcters before the end
for i in range(len(data) - 13):
	packet = data[i:i+14]
	if (is_unique(packet) == True):
		print(packet) # shows the packet for double checking
		print(i + 14) # get the last character processed
		break


# print(data)