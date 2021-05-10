#include <stdio.h>
int main()
{
    int n, a, b[1010], i, j, cnt, sum;
    while (scanf("%d%d", &n, &a) != EOF)
    {
        cnt = 0;
        for (i = 0; i < n; i++)
            scanf("%d", &b[i]);
        for (i = 0; i < n; i++)
        {
            sum = 0;
            for (j = i; sum < a; j++)
                sum += b[j];
            if (sum == a)
                cnt++;
        }
        printf("%d\n", cnt);
    }
}