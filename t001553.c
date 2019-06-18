#include<stdio.h>
int main()
{
    int T = 0;
    int i = 0;
    int m = 0;
    int n = 0;
    long long a[101][101];
    int j = 0;
    int k = 0;
    scanf("%d", &T);
    for(i = 0; i < T; i ++){
        scanf("%d %d", &n, &m);
        for(j = 0; j < n; j ++){
            for(k = 0; k < m; k ++){
                scanf("%lld", &a[j][k]);
            }
        }
        for(j = 0; j < m; j ++){
            for(k = 0; k < n; k ++){
              if(k == n - 1){
                  printf("%lld\n", a[k][j]);
              }
                else{
                printf("%lld ", a[k][j]);
                }
            }
        }
        printf("\n");
    }
}