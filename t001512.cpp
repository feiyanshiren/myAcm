#include<stdio.h>
#include<string.h>
int main()
{
    int n = 0;
    int i = 0;
    int h = 0;
    int a = 0;
    while (scanf("%d", &n) != EOF)
    {
        h = 0;
        for(i = 0; i < n; i++)
        {
            scanf("%d", &a);
            if(a >= 0)
            {
                h += a;
            }
            else
            {
                h += a * (i + 1);
            }
        }
        printf("%d\n", h);
    }
    return 0;
}