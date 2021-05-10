#include <stdio.h>
#include <stdlib.h>
int a[101], b[101];
int cmp(const void *a, const void *b)
{
    return *(int *)b - *(int *)a;
}
int main()
{
    int n, i;
    while (scanf("%d", &n) != EOF)
    {
        for (i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for (i = 0; i < n; i++)
            scanf("%d", &b[i]);
        qsort(a, n, sizeof(a[0]), cmp);
        qsort(b, n, sizeof(b[0]), cmp);
        for (i = 0; i < n; i++)
        {
            printf("%d ", a[i]);
            printf("%d ", b[i]);
        }
        printf("\n");
    }
    return 0;
}