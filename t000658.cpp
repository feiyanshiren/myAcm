#include<stdio.h>
#include<string.h>
int main()
{
    char s[100];
    int n;
    while(~scanf("%s%d",s,&n))
    {
        int l=strlen(s);
            n=n%l;
            printf("%s",s+l-n);
            for(int j=0;j<l-n;j++)
                printf("%c",s[j]);
        puts("");
    }
    return 0;
}
