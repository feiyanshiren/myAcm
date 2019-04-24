#include <stdio.h>
int main()
{
    int n,i,sum;
    char s[1000];
    scanf("%d",&n);
    getchar();
    while(n--)
    {
        gets(s);
        sum=0;
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]<0)
            {
                sum++;
                i++;
            }
        }
        printf("%d\n",sum);
    }
    return 0;
} 