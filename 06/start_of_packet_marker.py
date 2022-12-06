# read in data

# checks every packet if all are unique
def is_unique(packet):
	for i in range(4):
		for j in range(i + 1, 4):
			if (packet[j] == packet[i]):
				return False
	return True

file_obj = open("06.txt", "r")
data = file_obj.readlines()
data = data[0].strip() # removes newline

# reads until 4 charcters before the end
for i in range(len(data) - 3):
	packet = data[i:i+4]
	if (is_unique(packet) == True):
		print(packet) # shows the packet for double checking
		print(i + 4) # get the last character processed
		break


# print(data)