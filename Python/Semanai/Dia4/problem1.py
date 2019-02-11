import sys

def dfs(cur,ret):
    print(f'cur = {cur}')
    if array[cur]:
        ret+=1
    else:
        ret = 0
    if ret > m or visited[cur]:
        return False
    visited[cur]=1
    if (cur > 1 and len(v[cur])==1):
        return True
    ans=0
    for i in range(0,len(v[cur])):
        ans+=dfs(v[cur][i],ret)
        print(ans)
    return ans

v = []
l=[]

for i in range(100005):
    v.append(l)

visited = []
for i in range(100005):
    visited.append(0)

n,m = map(int,sys.stdin.readline().split())

array=input().split(' ')
for i in range(len(array),1000005-len(array)):
    array.append(0)



for i in range (n-1):
    n1,n2 = map(int,sys.stdin.readline().split())
    v[n1].append(n2)
    v[n2].append(n1)

print(dfs(1,0))
