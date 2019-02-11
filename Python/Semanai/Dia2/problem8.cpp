#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
    int n,m;
    int a[100005];
    int b[100005];
    int Hash[100005];
    while(scanf("%d%d",&n,&m)!=EOF)
    {
        int cnt=0;
        memset(Hash,0,sizeof(Hash));
        for(int i=1;i<=n;i++) scanf("%d",&a[i]);
        for(int i=n;i>=1;i--)
        {
            if(!Hash[a[i]]) cnt++;
            Hash[a[i]]=1;
            b[i]=cnt;
        }
        while(m--)
        {
            int x;
            scanf("%d",&x);
            printf("x vale,m vale :%i %i\n",x,m);
            //printf("m vale :%i\n",m);
            printf("%d\n",b[x]);
        }
    }
    return 0;
}
