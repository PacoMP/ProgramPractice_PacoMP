import sys

n,m = map(int,sys.stdin.readline().split())
listi = input().split(' ')
listm=[]
checklist = []
for i in range(0,m):
    listm.append(input())



for i in range(0,m):
    aux=listi[:]
    for j in range(1,int(listm[i])):
        aux.pop(0)
    uniques=set(aux)
    #print(uniques)
    print(len(uniques))
