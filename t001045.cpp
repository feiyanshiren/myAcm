/****************
Times:28ms.
****************/
#include<stdio.h>
int a[20005];
int main()
{
    int n,T;
    scanf("%d",&T);
    while(T--)
    {
        int q,maxx=-1;
        scanf("%d",&n);
        for(int i=0; i<n; i++)
        {
            scanf("%d",&a[i]);
            if(maxx<a[i])
            {
                q=i,maxx=a[i];
            }
        }
        int sum=1;
        for(int i=q-1; i>=0; i--)
        {
            int f=1;
            for(int j=0; j<i; j++)
            {
                if(a[j]>a[i])
                {
                    f=0;
                    break;
                }
            }
            if(f) sum++;
        }
        for(int i=q+1; i<n; i++)
        {
            int f=1;
            for(int j=n-1; j>i; j--)
            {
                if(a[j]>a[i])
                {
                    f=0;
                    break;
                }
            }
            if(f) sum++;
        }
        printf("%d\n",sum);
    }
}
