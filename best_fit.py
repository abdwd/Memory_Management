###### for testing #########
from initial import *

import copy

# Function to allocate memory to blocks by best fit
def bestFit(memory_arr, process, name):

	memory = copy.deepcopy(memory_arr)
	backup_mem = copy.deepcopy(memory_arr)
	n = len(process)
	
	# Stores block id of the block
	# allocated to a process
	allocation = [False] * n
	
	# pick each process and find suitable
	# blocks according to its size ad
	# assign to it
	for i in range(n):
		
		# Find the best fit block for
		# current process
		bestIdx = -1
		for j in range(len(memory)):
			if memory[j][2] == 'free':
				if (memory[j][1]-memory[j][0]+1)  >= process[i][1]:
					if bestIdx == -1:
						bestIdx = j
					elif (memory[bestIdx][1]-memory[bestIdx][0]) > (memory[j][1]-memory[j][0]):
						bestIdx = j

		# If we could find a block for
		# current process
		if bestIdx != -1:
			
			# allocate True to p[i] process
			allocation[i] = True

			# Reduce available memory in this block.
			memory[bestIdx][2] = name +  '(' + process[i][0] + ')'
			memory.insert(bestIdx + 1, [memory[bestIdx][0] + process[i][1], memory[bestIdx][1], 'free'])
			memory[bestIdx][1] = memory[bestIdx][0] + process[i][1] - 1

	done = 1
	for i in range(n):
		if allocation[i] == False:
			done = 0
			break
	if done == 1:
		backup_mem = memory
	return done, backup_mem


if __name__ == '__main__':
	#block entry [ [start,end ,free] ]
	h = [[400, 125], [100, 250], [1000, 500],[550,450] ]
	z = intialAlloc(1500, h)
	print(z)
	processSize = [['code',212] ,
				   ['IDE', 426],
				   ['data',417] ,
				   ['stack',112],
				   ['zz',12]]
	result, mymem = bestFit(z, processSize, 'p1')
	print(result)
	print(mymem)