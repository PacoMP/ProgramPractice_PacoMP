
import sys

#========MAIN=============
n = int(input())
k = list(str(input()))
a = []


for i in range(100000):
    a.append(0)


Klength = len(k)
ans = 0
for i in range(0,Klength):
    a[i] = int(k[i])
    ans += a[i]
a.sort()
#print(ans)
#print(a)
sum = 0
if ans >= n:
    print("0")
    sys.exit(0)
for i in range(0,Klength):
    sum += 1
    #print(a[-Klength+i])
    ans += 9 - a[-Klength+i]
    #print(ans)
    if ans >= n:
        print(sum)
        break
