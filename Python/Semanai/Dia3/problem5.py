import sys

array=[]
for i in range(1010):
    array.append(0)

n,x0,y0 = map(int,sys.stdin.readline().split())

cnt = 0
res = 0
flag = 0
for i in range(0,n):
    x,y = map(int,sys.stdin.readline().split())
    dx = x-x0
    dy = y-y0
    if not flag and dx==0:
        flag = 1
        res+=1
    elif(dx!=0):
        #print('entre')
        cnt=cnt+1
        array[cnt]=int(dy/dx)

#print(array)
#print(f'count={cnt}')

array2 = []

for i in range(1,cnt+1):
    array2.append(array[i])

array2.sort()
print(array2)
#print(cnt)
for i in range(0,cnt):
    while array[i]==array[i+1] and i < cnt-1:
        print('entre')
        i+=1
    res+=1

print(res)
