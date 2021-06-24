###### for testing #########
from first_fit import *
from best_fit import *
from initial import *
############################
import copy

def compaction (memory_arr):

    memory = copy.deepcopy(memory_arr)
    mem_size = memory[-1][1]
    temp=[]
    for i in range( len(memory)):
        if memory[i][2] != 'free':
            temp.append(memory[i].copy())

    index =0
    for i in range (len(temp)):
        size = temp[i][1]-temp[i][0]
        temp[i][0]=index
        index += size
        temp[i][1] = index
        index +=1
    temp.append([index,mem_size,'free'])
    return temp


if __name__ == '__main__':
    #block entry [ [start,end ,free] ]
    h = [[400, 125], [100, 250], [1000, 500],[550,450] ]
    z = intialAlloc(1500, h)
    print(z)
    processSize = [['code',212],
				   ['IDE', 426],
				   ['data',417] ,
				   ['stack',112],
				   ['zz',12]]
    result, mymem = bestFit(z, processSize, 'p1')
    print(result)
    print(mymem)
    mem=compaction(mymem)
    print(mem)

