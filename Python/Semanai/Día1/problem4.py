

a = []
for i in range(1000005):
    a.append(0)

n = int(input())
ans = n


for i in range(2,n+1):
    if not a[i]:
        j = 2*i
        while(j <= n):
            a[j] = i
            j+=i
    a[i] = i - a[i] +1

#print (a)

for i in range(a[n],n+1):
    ans = min(ans,a[i])
    #print (ans)

print(ans)
