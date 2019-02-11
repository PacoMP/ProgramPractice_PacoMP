import sys


#===================MAIN===========
S,v1,v2,t1,t2 = map(int,sys.stdin.readline().split())
P1 = 2*(t1) + (S*v1)
P2 = 2*(t2) + (S*v2)
if(P1 < P2):
    print("First")
if(P2 < P1):
    print("Second")
if(P2 == P1):
    print("Friendship")
