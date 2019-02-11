import sys
import itertools


numInp = [int(x) for x in input()]
aux = numInp[:]
#print(aux)
num = 0
newNum = 0
flagVuelta=False
for i in range(0,len(numInp)):
    joinNum = 0
    aux = numInp[:]
    if(len(numInp) != 1 and flagVuelta=False):
        aux.pop(i)
    if(i = len(numInp)):
    #print(aux)
    #print(numInp)
    for j in aux:
        joinNum = joinNum*10 + j
    #print(joinNum)
    if((joinNum%8)==0):
        ans=joinNum
        message=True
        break
    else:
        message=False



if(message == True):
    print('YES')
    print(ans)
else:
    for i in range(0,len(numInp)):
        if((numInp[i]%8)==0):
            print('YES')
            print(numInp[i])
            break
        else:
            print('NO')
            break
