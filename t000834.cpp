#include <stdio.h>
int main()
{
    int n[55],i,k,N;
    while(scanf("%d",&N)!=EOF)
    {
        int t=0,s=0;
       for(i=1;i<=N;i++)
       scanf("%d",&n[i]);
       while(t++<3)
       {
        k=1;
        for(i=2;i<=N;i++)
        if(n[i]>n[k])
        k=i;
        s+=n[k];
        n[k]=0;
        }
        for(i=1;i<=N;i++) 
        if(!n[i])
        printf("%d ",i);
        printf("%d\n",s);
        }
        return 0;
    }