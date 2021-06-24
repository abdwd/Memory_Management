# Function to initialize the memory

def intialAlloc(size,holes):
    mem =[]
    index=0
    holes=sorted(holes,key=lambda l:l[0])
    if holes[0][0]==0:
        mem.append([0,holes[0][1]-1,'free']) #free
        for i in range (1,len(holes)):
            if holes[i][0] != mem[-1][1]+1:
                mem.append([mem[-1][1]+1, holes[i][0]-1, 'old'+ str(index) + '()']) #full
                index +=1
                mem.append([holes[i][0], holes[i][0] + holes[i][1] - 1, 'free'])  # free
            elif (holes[i][0] == mem[-1][1] + 1) and (mem[-1][2] == 'free'):
                mem[-1][1] += holes[i][1]
            else:
                mem.append([holes[i][0], holes[i][0] + holes[i][1] - 1, 'free'])  # free
    else:
        mem.append([0, holes[0][0]-1,  'old' +str(index) + '()']) #full
        index += 1
        for i in range (0,len(holes)):
            if holes[i][0] != mem[-1][1]+1:
                mem.append([mem[-1][1]+1, holes[i][0]-1, 'old'+ str(index) + '()']) #full
                index += 1
                mem.append([holes[i][0], holes[i][0] + holes[i][1] - 1, 'free'])  # free
            elif ( holes[i][0] == mem[-1][1]+1) and ( mem[-1][2]=='free') :
                mem[-1][1]+= holes[i][1]
            else :
                mem.append([holes[i][0], holes[i][0] + holes[i][1] - 1, 'free'])  # free

    if mem[-1][1]!= size-1:
        mem.append([mem[-1][1] + 1, size - 1, 'old' + str(index) + '()'])  # full
    
    return mem

if __name__ == '__main__':
    h= [ [300,200] ,[100,200],[800,100]   , [1400,10],[0,100]     ]
    y=intialAlloc(1500, h)
    print(y)

#[[0, 99, 'old0'], [100, 299, 'free'], [300, 499, 'free'], [500, 799, 'old1'], [800, 899, 'free'], [900, 1399, 'old2'],
# [1400, 1498, 'free'], [1499, 1499, 'old3']]
