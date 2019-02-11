import sys

def WeirdSub(a,b):
    while a != 0 and b != 0:
        if a>=(2*b):
            a%= 2*b
            #WeirdSub(a,b)
        elif b>=(2*a):
            b%= 2*a
            #WeirdSub(a,b)
        else:
            break
    return a,b

#===================MAIN===========
#sys.setrecursionlimit(1500)
a,b = map(int,sys.stdin.readline().split())
#print(f"{a},{b}")
l=list(WeirdSub(a,b))
a=l[0]
b=l[1]
print(a,b)
