import sys
import copy


listm=[]

visited=[]
for i in range(100002):
    visited.append(0)

checklist = []
for i in range(100002):
    checklist.append(0)


#===========MAIN==========

n,m = map(int,sys.stdin.readline().split())
listi = input().split(' ')

for i in range(0,m):
    listm.append(input())

count=0
i=n-1
#print(len(listi))
while(i>=0):
    #print("entre")
    value = int(listi[i])
    if not (checklist[value]):
        count+=1
    checklist[value] = 1
    visited[i]=count
    #print(count)
    i-=1
x=1

#print(visited)

while(m>0):
    for number in listm:
        #print(f"numero{number}")
        print(visited[int(number)-1])
        m-=1
