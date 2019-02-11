import sys

def fastpow(base, exp):
    """ Fast power calculation using repeated squaring """
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

'''
def fastpow(a,b):
    ret=1
    while(b>0):
        if(b&1):
            ret = ret + a
        a = a*a
        b = b>>1
    return ret
'''
#=============MAIN======================
n,a,b,k = map(int,sys.stdin.readline().split())
input2 = list(input())
total_sum=0
modulo = 1000000009
if len(input2) <= k :
    for i in range(n+1):
        if input2[0] == '+':
            s=1
        else:
            s=-1
        #print(f's={s}')
        total_sum += s*(int(fastpow(a,n-i)))*int(fastpow(b,i))
        if(len(input2) != 1):
            input2.pop(0)
        #print(input2)

print(total_sum%modulo)
