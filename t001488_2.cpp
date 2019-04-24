#include <stdio.h>
int main()
{
    int i,sum;
    char s[1000];
    while(gets(s) != NULL)
    {
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
