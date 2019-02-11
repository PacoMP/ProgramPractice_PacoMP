mod = 1000000007

def pow1(a,b):
    ans = 1
    c=a
    while(b):
        #print('estoy en el while')
        if(b & 1):
            ans=ans*c%mod
        b>>=1
        c=c*c%mod
    return ans



def factorial(a,b):
    factor =fact[a]*pow1(fact[b]*fact[a-b]%mod,mod-2)%mod
    return factor


fact = []
for i in range(1000010):
    fact.append(0)

a = []
for i in range(1010):
    a.append(0)

#================MAIN===============
fact[0] = 1

for i in range(1,1000000):
    fact[i]=fact[i-1]*i%mod

n = int(input())
#print(n)
sum = 0

for i in range(0,n):
    a[i] = int(input())
    sum+=a[i]
#print (a)
#print(sum)
ans = 1
i = n-1
while(i>-1):
    ans=ans*factorial(sum-1,a[i]-1)%mod
    #print(ans)
    sum-=a[i]
    i-=1
    #print(f"suma:{sum}")

print(ans)
