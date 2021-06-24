###### for testing #########
from initial import *

import copy
# Function to allocate memory to blocks by first fit

def firstFit(memory_arr, process,name):

	memory = copy.deepcopy(memory_arr)
	backup_mem = copy.deepcopy(memory_arr)
	n = len(process)
	# Stores block id of the
	# block allocated to a process
	allocation = [False] * n

	# Initially no block is assigned to any process

	# pick each process and find suitable blocks
	# according to its size ad assign to it
	for i in range(n):
		for j in range(len(memory)):
			if memory[j][2]=='free':

				if ((memory[j][1]- memory[j][0] )+1) == process[i][1]:

					allocation[i] = True


					memory[j][2] = name + '(' + process[i][0] + ')'

					break

				elif ((memory[j][1]- memory[j][0])+1) >process[i][1]:

					allocation[i] = True

					# Reduce available memory in this block.
					memory[j][2] = name + '(' + process[i][0] + ')'
					memory.insert(j + 1, [memory[j][0]+ process[i][1],memory[j][1],'free'])
					memory[j][1] = memory[j][0]+ process[i][1]-1
					break
	done = 1
	for i in range(n):
		if allocation[i] == False:
			done=0
			break
	if done == 1 :
		backup_mem=memory
	return done, backup_mem

if __name__ == '__main__':
	#block entry [ [start,end ,free] ]
	h = [[500, 450], [100, 350], [1000, 500] ]
	z = intialAlloc(1500, h)
	print(z)
	processSize = [['code',212] ,
				   ['IDE', 426],
				   ['data',417] ,
				   ['stack',112],
				   ['zz',12]]
	result, mymem = firstFit(z, processSize, 'p1')
	print(result)
	print(mymem)
