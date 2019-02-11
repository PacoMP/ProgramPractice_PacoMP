import sys


n,m = map(int,sys.stdin.readline().split())
counter = 0

if n > m:
    counter=n-m
else:
    while (m-n)!=0 :
        if(m%2==0 and m>n):
            m/=2
            counter+=1
        else:
            if(n>=m):
                counter+=n-m
                break
            m=(m+1)/2
            counter+=2

print(int(counter))
