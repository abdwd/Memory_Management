###### for testing #########
from first_fit import *
from best_fit import *
from worst_fit import *
from initial import *
from dealloc import *
############################
import matplotlib.pyplot as plt
import copy

def legend_without_duplicate_labels(ax):
    handles, labels = ax.get_legend_handles_labels()
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    ax.legend(*zip(*unique))


def plot(mem_arr):
    memory = copy.deepcopy(mem_arr)
    n = len(memory)
    size = memory[-1][1]
    yTick = []
    yTicklabel=[]
    temp=[]
    for i in range(n):
        yTick.append(memory[i][0])
        yTicklabel.append(memory[i][2]+'  ' +str(memory[i][0]))
        if memory[i][2]!= 'free':
            l=memory[i][2].find('(')
            if memory[i][2][:l] not in temp:
                temp.append(memory[i][2][:l])
    process = []
    for i in range(len(temp)):
        row=[]
        for j in range(n):
            if len(temp[i])<len (memory[j][2]):
                l= len(temp[i])
                if temp[i]== memory[j][2][:l]:
                    row.append([( memory[j][0] ,memory[j][1] -memory[j][0]  ),memory[j][2]])
        process.append(copy.deepcopy(row))
    row = []
    for i in range (n):
        if memory[i][2] == 'free':
            row.append([( memory[i][0] ,memory[i][1] -memory[i][0]  ),memory[i][2]])
    process.append(copy.deepcopy(row))
    temp.append('free')

    #plt.ion()
    fig, gnt = plt.subplots()
    gnt.set_xlim(0,3 )
    gnt.set_xticks([])
    gnt.set_xticklabels([])
    gnt.set_ylim(size, 0)
    gnt.set_ylabel('byte')
    gnt.set_yticks(yTick)
    gnt.set_yticklabels(yTicklabel)
    plt.xticks(rotation=90)
    colors = ['red','pink' ,'blue', 'purple','cyan', 'limegreen', 'darkorange','midnightblue']


    for i in range(len(process)-1):
        for j in range (len(process[i])):
            gnt.broken_barh([(0,1)], process[i][j][0], color=colors[i], label=temp[i] )

    for j in range(len(process[-1])):
        gnt.broken_barh([(0, 1)], process[-1][j][0], color='lightgrey', label='free')
    #plt.setp(gnt.get_yticklabels(),  horizontalalignment='right', fontsize='x-small')
    #fig.set_size_inches(5.5, 9)
    plt.tight_layout()
    plt.legend()
    legend_without_duplicate_labels(gnt)
    plt.show()
    #plt.show()



if __name__ == '__main__':
    #block entry [ [start,end ,free] ]
    h = [[400, 125], [100, 250], [1000, 500],[550,450] ]
    z = intialAlloc(1500, h)
    print(z)
    processSize = [['code',212],
				   ['IDE', 226],
				   ['data',217] ,
				   ['stack',112],
				   ['zz',12]]
    result, mymem = bestFit(z, processSize, 'p1')
    #print(result)
    #print(mymem)
    plot(mymem)
    z = input()

    mymem = deallocate('old0', mymem)
    print(" My Mem")
    print(mymem)
    plt.close()
    plot(mymem)
    z=input()

    er=deallocate('p1', mymem)
    plt.close()
    plot(er)
    z=input()


