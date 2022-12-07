
def	traverse(data, i, size, size_answer):
	if (len(data[i]) == 0 ):
		return size_answer
	command = data[i].split(" ")
	if (command[1] == "cd" and command[2] == ".."):
		if (size <= 100000):
			size_answer += size
		return size_answer
	elif (command[0].isdigit() == True):
		size += int(command[0])
	size = traverse(data, i + 1, size, size_answer)
	return size_answer
	

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

size_answer = traverse(data, 0, 0, 0)

print("puzzle answer:")
print(size_answer)



