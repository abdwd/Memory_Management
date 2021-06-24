###### for testing #########
from initial import *

import copy

# Function to allocate memory to blocks by worst fit
def worstFit(memory_arr, process, name):

	memory = copy.deepcopy(memory_arr)
	backup_mem = copy.deepcopy(memory_arr)
	n = len(process)

	# Stores block id of the block
	# allocated to a process
	allocation = [False] * n

	# pick each process and find suitable blocks
	# according to its size ad assign to it
	for i in range(n):
		
		# Find the best fit block for
		# current process
		wstIdx = -1
		for j in range(len(memory)):
			if memory[j][2] == 'free':
				if (memory[j][1]-memory[j][0]+1)  >= process[i][1]:
					if wstIdx == -1:
						wstIdx = j
					elif (memory[wstIdx][1]-memory[wstIdx][0]) < (memory[j][1]-memory[j][0]):
						wstIdx = j

		# If we could find a block for
		# current process
		if wstIdx != -1:
			
			# allocate True to p[i] process
			allocation[i] = True

			# Reduce available memory in this block.
			memory[wstIdx][2] = name +  '(' + process[i][0] + ')'
			memory.insert(wstIdx + 1, [memory[wstIdx][0] + process[i][1], memory[wstIdx][1], 'free'])
			memory[wstIdx][1] = memory[wstIdx][0] + process[i][1] - 1

	done = 1
	for i in range(n):
		if allocation[i] == False:
			done = 0
			break
	if done == 1:
		backup_mem = memory
	return done, backup_mem

if __name__ == '__main__':
	# block entry [ [start,end ,free] ]
	h = [[650,500 ], [100, 500], [1200, 500], [2000, 450]]
	z = intialAlloc(15000, h)
	print(z)
	processSize = [['code', 212],
				   ['IDE', 426],
				   ['data', 417],
				   ['stack', 112],
				   ['zz', 12]]
	result, mymem = worstFit(z, processSize, 'p1')
	print(result)
	print(mymem)