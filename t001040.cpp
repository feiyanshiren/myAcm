#include<stdio.h>

int main()

{

    int i,j,cnt,k,N,K,a[5555];

    scanf("%d%d",&N,&K);

    int ans=0;

    for(i=1;i<=N;i++) scanf("%d",&a[i]);

    for( i=1;i<=N;i++)

      for(j=i+1;j<=N;j++)

       {

           cnt=0;

           for( k=i;k<=j;k++) cnt+=a[k];

           if(cnt%K==0) ans++;

       }

    printf("%d\n",ans);

}