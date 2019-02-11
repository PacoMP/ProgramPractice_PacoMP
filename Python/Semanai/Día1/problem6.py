import sys


#=========MAIN==========
number = int(input())
input2 = [int(x) for x in input().split()]
print(input2)
if (number%2 == 0 or input2[0]%2==0 or input2[-1]%2==0):
    print("No")
else:
    print("Yes")
