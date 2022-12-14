# read in data
file_obj = open("07.txt", "r")
data = file_obj.readlines()
#strip newlines
for i in range(len(data)):
	data[i] = data[i].strip()

size_answer = 0

folder_sizes = []
total_folder_size = 0
for i in range(len(data)):
	command = data[i].split(" ") # split command into tokens
	print(command)
	if ((len(command) == 3 and command[2] == ".." and len(folder_sizes) > 0) or
		i == len(data) - 1):
		for j in range(len(folder_sizes)):
			total_folder_size += folder_sizes[j]
		if (total_folder_size <= 100000):
			size_answer += total_folder_size
		print("Folder sizes:")
		print(folder_sizes)
		print("size:")
		print(size_answer)
		total_folder_size = 0
		folder_sizes = []
	elif (command[0].isdigit() == True):
		folder_sizes.append(int(command[0]))

print("puzzle answer:")
print(size_answer)

# not 1276418 ?