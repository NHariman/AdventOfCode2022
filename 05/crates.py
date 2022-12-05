# [P]     [L]         [T]            
# [L]     [M] [G]     [G]     [S]    
# [M]     [Q] [W]     [H] [R] [G]    
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]
#  1   2   3   4   5   6   7   8   9 

# parses the "move 8 from 3 to 2" part to extract the numbers and save it to a list
def get_action(input):
	amount = [int(i) for i in input.split() if i.isdigit()]
	return amount

# transposes the depot list so the first element in the list is the top one
# and every unit is now one stack
def transpose(depot):
	unit = []
	new_depot = []
	for i in range(9):
		for j in range(8):
			if (depot[j][i] != " "):
				unit.append(depot[j][i])
		new_depot.append(unit)
		unit = []
	return new_depot

# executes the move from one stack (from_stack) to the other stack (to_stack)
# for the amount mentioned in the move action, pop the first element (which is the top of the stack)
# and insert it into the top of the to_stack list.
def execute_action(action, depot):
	from_stack = action[1] - 1
	to_stack = action[2] - 1
	for i in range(action[0]):
		pop = depot[from_stack].pop(0)
		depot[to_stack].insert(0, pop)
	return depot
	
# read in the data
file_obj = open("05.txt", "r")
data = file_obj.readlines()

unit = []
depot = []
new_depot = []
# increments of four, grab the initial state of the boxes
# but its done by row instead of column so each row isn't representative to a stack
for j in range(8):
	for i in range(1, 36, 4):
		unit.append(data[j][i])
	depot.append(unit)
	unit = []

# transpose so every unit is one stack
new_depot = transpose(depot)
# print(new_depot)

# get actions and execute the changes
final_state = []
size = len(data)
for i in range(10, size):
	if (len(data[i]) == 1):
		break
	action = get_action(data[i])
	final_state = execute_action(action, new_depot)

#prints out results
for i in range(9):
	print(final_state[i][0], end="")
print("")
