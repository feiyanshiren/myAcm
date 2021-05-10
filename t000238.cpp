#include <cstdio>//最优codes
int main()
{
    int n,T;
    scanf("%d",&T);
    while(T--)
    {
        int Max=1<<31,Min=9999999,x;
        scanf("%d",&n);
        while(n--)
        {
            scanf("%d",&x);
            if(x>Max)
                Max=x;
            if(x<Min)
                Min=x;
        }
        printf("%d\n",Max-Min);
    }
    return 0;
}
