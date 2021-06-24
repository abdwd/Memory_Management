###### for testing #########
from first_fit import *
from initial import *
############################
import copy

# Function to deallocate processes from memory
def deallocate( name , memory_arr ):
    memory = copy.deepcopy(memory_arr)
    l = len(name)
    n = len(memory)
    for i in range (n):
        if len(memory) <= i:
            break
        if len(memory[i][2])> l:
            if ( memory[i][2][:l] == name ) and (memory[i][2][l] =='(') :
                if i == 0 :
                    if memory[i+1][2] == 'free':
                        memory[i+1][0] = memory[i][0]
                        memory.pop(i)
                    else :
                        memory[i][2]= 'free'

                elif i < ( len(memory) -1) :
                    if (memory[i-1][2] == 'free') and ( memory[i+1][2] == 'free'):
                        memory[i-1][1] = memory[i+1][1]
                        memory.pop(i)
                        memory.pop(i)

                    elif memory[i-1][2] == 'free':
                        memory[i-1][1] = memory[i][1]
                        memory.pop(i)
                    elif memory[i+1][2] == 'free':
                        memory[i + 1][0] = memory[i][0]
                        memory.pop(i)
                    else :
                        memory[i][2]='free'
                else :
                    if memory[i - 1][2] == 'free':
                        memory[i - 1][1] = memory[i][1]
                        memory.pop(i)
                    else :
                        memory[i][2]='free'

    for i in range (len(memory)):
        if len(memory) <= i:
            break
        if len(memory[i][2]) > l:
            if (memory[i][2][:l] == name) and (memory[i][2][l] == '('):
                memory = deallocate(name, memory)
                break

    return memory
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
    result, mymem = firstFit(z, processSize, 'p1')
    print(result)
    print(mymem)
    deal= deallocate( 'p1' , mymem )
    print (deal)
    mem = deallocate('old1', deal)
    print(mem)
    mem = deallocate('old0', mem)
    print(mem)
    mem = deallocate('old2', mem)
    print(mem)




