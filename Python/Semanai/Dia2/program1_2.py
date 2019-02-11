import sys
import itertools


numInp = [int(x) for x in input()]
aux = numInp[:]
#print(aux)
num = 0
newNum = 0
message = False

list1=itertools.combinations(numInp,1)
list2=itertools.combinations(numInp,2)
list3=itertools.combinations(numInp,3)
#print(list(list1))
#print(list(list2))
#print(list(list3))

#3s combiantions
for combinations in list3:
    joinNum=0
    #print(combinations)
    for numbers in range(0,len(combinations)):
            joinNum = joinNum*10 + combinations[numbers]
            #print(joinNum)
    if((joinNum%8)==0):
        ans=joinNum
        message=True
        break
    else:
        message=False

if(message == False):
    #2s combiantions
    for combinations in list2:
        joinNum=0
        for numbers in range(0,len(combinations)):
                joinNum = joinNum*10 + combinations[numbers]
                #print(joinNum)
        if((joinNum%8)==0):
            ans=joinNum
            print('YES')
            print(ans)
            sys.exit(0)
            break
        else:
            message=False
    if(message == False):
        #1s commbinations
        for combinations in list1:
            if((combinations[0]%8)==0):
                #print(combinations[0])
                ans=combinations[0]
                message=True
                break
            else:
                message=False
        if(message == False):
            print('No')
        else:
            print('YES')
            print(ans)
else:
    print('Yes')
    print(ans)
