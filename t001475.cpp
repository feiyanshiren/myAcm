#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *revstr(char *str, size_t len)
{
    char    *start = str;
    char    *end = str + len - 1;
    char    ch;

    if (str != NULL)
    {
        while (start < end)
        {
            ch = *start;
            *start++ = *end;
            *end-- = ch;
        }
    }
    return str;
}

int main()
{
    int T, n, i, j;
    char a[100];
    char s[100];
    char b[20][200];
    scanf("%d", &T);
    for(i = 0; i < T; i ++)
    {
    	scanf("%d", &n);
    	for(j = 0; j < n; j ++)
    	{
    		scanf("%s", a);
            strcpy(s, a);
            revstr(s, n);
            strcpy(b[j], a);
            strcat(b[j], s);
    	}
        for(j = 0; j < n; j ++)
        {
            printf("%s\n", b[j]);
        }
        for(j = n - 1; j >= 0; j --)
        {
            printf("%s\n", b[j]);
        }
    }
    return 0;
}