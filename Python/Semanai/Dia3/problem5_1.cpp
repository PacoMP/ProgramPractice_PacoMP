#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

double a[1010];

int main(){
    int n,i,x,y;
    int xx,yy;
    int cnt,res;
    int flag;
    while(~scanf("%d %d %d",&n,&x,&y)){
    	cnt=res=0;
     	flag=0;
        for(i=0;i<n;i++){
            scanf("%d %d",&xx,&yy);
            double jx=xx-x;
            double jy=yy-y;
            if(!flag&&jx==0){
                flag=1;
                res++;
            }
            else if(jx!=0){
                a[cnt++]=jy/jx;
            }
        }
        sort(a,a+cnt);


        for(i=0;i<cnt;i++){
        	while(a[i]==a[i+1]&&i<cnt){
	        	i++;
	        }
        	res++;
        }
        printf("%d\n",res);
    }
    return 0;
}
