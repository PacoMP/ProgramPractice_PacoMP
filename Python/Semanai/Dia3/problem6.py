import sys

n,p,q = map(int,sys.stdin.readline().split())
word = list(input())

sol = -1

for i in range(0,int(n/p)+1):
    #print(i)
    #print(f'sol={sol}')
    for j in range(0,int(n/q)+1):
        #print(j)
        if((i*p+j*q)==n):
            #print('entre')
            sol = i+j
            print(sol)
            for k in range(0,n):
                sys.stdout.write(word[k])
                if(i and k<i*p and not((k+1)%p) or j and k>=i*p and not((k-i*p+1)%q)):
                    print("")
            sys.exit(0)
        if(sol!=-1):
            break

if(sol==-1):
    print('-1')
