#include<stdio.h>
int main() {
  int n, m;
  while(scanf("%d%d", &n, &m) != EOF) {
    int t[100005], max = 0;
    for(int i = 0; i < n; i++)
      scanf("%d", &t[i]);
    for(int i = 0; i < n; i++) {
      int temp = m, sum = 0;
      for(int j = i; j < n && temp >= 0; j++) {
        temp -= t[j];
        if(temp >= 0) sum++;
      } 
      if(sum > max) max = sum;
    }
    printf("%d\n", max);
  }
}
