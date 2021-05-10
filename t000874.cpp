#include<stdio.h>
int main()
{
    int a,b,z;
    while(~scanf("%d %d",&a,&b))
    {
        int sum = a;
        z = 0;
        for(int i = 1; i <= b; i ++)
        {
            z++;
            if(z % 5 == 0)
            {
                sum = sum + 6;
                z = 1;
            }
            else
            {
                sum = sum + 1;
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}