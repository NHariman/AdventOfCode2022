# when a cd command is found that's not a cd ..
# then the following command will be ls, therefore
# save the cd directory name, skip over ls
# and start saving directories in said file
# and tally any file sizes in there.
# this should return a size total that can then be returned
# for evaluation if it's smaller or equal to 100.0000
def		shell_command(command, data, start_point):
	keys = ["directory_name", "sub_dirs", "size"]
	folder = dict.fromkeys(keys)
	sub_dirs = []
	size = 0

	folder.update({"directory_name": command[2]})
	i = start_point + 2
	while (i <= len(data) - 1 and data[i][0] != '$'):
		file_obj = data[i].split(" ")
		if (file_obj[0] == "dir"):
			sub_dirs.append(file_obj[1])
		elif (file_obj[0].isdigit() == True):
			size += int(file_obj[0])
		i += 1
	folder.update({"sub_dirs": sub_dirs})
	folder.update({"size": size})
	print(folder)
	return i, folder, size

# read in data
file_obj = open("07.txt", "r")
data = file_obj.readlines()
#strip newlines
for i in range(len(data)):
	data[i] = data[i].strip()

# make file_structure list that contains directories and the size 
# [ "directory_name", "sub_directories", "size"]
# maybe make this a dictionary?
# cd [letters] = new recursion call
# cd .. = return recursion call
# ls ignore?
# dir = create list with first element 

size_answer = 0
size = 0
directories = []
folder = {}
for i in range(len(data)): # loop through data
	command = data[i].split(" ") # split command into tokens
	if (command[1] == "cd" and command[2] != ".."): # if not a backspace, parse the shell command
		i, folder, size = shell_command(command, data, i) # returns the new position of i, the folder dict with the info in it, and the size of the folder
		size = 0 # reset everything
		directories.append(folder) # append folder to the dictionaries
		folder = {}

# total size of each subdirectory with main directory
for directory in directories:
	if (directory['size'] <= 100000):
		size_answer += directory['size']
	elif (len(directory['sub_dirs'])):
		size = 0
		for item in directories:
			if (item['directory_name'] == directory['directory_name']):
				size += item['size']
				break
		



print("puzzle answer:")
print(size_answer)



