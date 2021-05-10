#include <stdio.h>
#include <string.h>
int k[150];
int main()
{
    memset(k, 0, sizeof(k));
    int n;
    scanf("%d", &n);
    while (n)
    {
        n = n - 1;
        int i;
        scanf("%d", &i);
        k[i] = k[i] + 1;
    }
    for (int i = 0; i <= 150; i++)
    {
        for (int j = 0; j < k[i]; j++)
        {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}
