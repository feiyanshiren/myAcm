#include <bits/stdc++.h>
using namespace std;
struct gun{
    int p;
    int k;
    int kind[1010];
};
gun g[1010];
double pei[1010];
int main(){
    int n, m;
    while (scanf("%d%d", n, m) != EOF){
        for (int i = 0; i < 1010; i ++)
            pei[i] = 0;
        for (int i = 0; i < n; i ++){
            scanf("%d", g[i].p);
            scanf("%d", g[i].k);
            for (int j = 0; j < g[i].k; j ++)
                scanf("%d", g[i].kind[j]);
        }
        for (int i = 0; i < m; i ++){
            int q;
            double b;
            scanf("%d", q);
            scanf("%lf", b);
            if(pei[q] < b){
                pei[q] = b;
            }
        }
        double maxn = 0;
        for (int i = 0; i < n; i ++){
            double temp = 1;
            for (int j = 0; j < g[i].k; j ++){
                temp += pei[g[i].kind[j]];
            }
            if (g[i].p * temp > maxn)
                maxn = g[i].p* temp;
        }
        printf("%.4lf\n", maxn);
    }
    return 0;
}