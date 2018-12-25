#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
 
vector<int> v[205];
 
int n, m;
int vis[205];
int x;
 
void dfs(int u)
{
    for (int i = 0; i < v[u].size(); i++){
        if (vis[v[u][i]] == 0){
            vis[v[u][i]] = (vis[u] == 1 ? 2 : 1);
            dfs(v[u][i]);
        }
        else if (vis[v[u][i]] == vis[u]){
            x = 0;
            return;
        }
    }
    return;
}
 
int main()
{
    int a, b;
    while (scanf("%d", &n) != EOF){
        scanf("%d", &m);
        x = 1;
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < m; i++){
            scanf("%d%d", &a, &b);
            v[a].push_back(b);
            v[b].push_back(a);
        }
        vis[0] = 1;
        dfs(0);
        if (x)
            printf("BICOLORABLE.\n");
        else
            printf("NOT BICOLORABLE.\n");
 
        for (int i = 0; i <= n; i++)
            v[i].clear();
    }
    return 0;
}
