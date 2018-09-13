#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
 int n;
 scanf("%d",&n);
 while(n--)
 {
  double a[7],sum=0;
  int i;
  for(i=0;i<7;i++)
  {
   scanf("%lf",&a[i]);
  }
  sort(a,a+7);
  sum=(a[0]+a[3]+a[6])/3;
  printf("%.2lf\n",sum);
 }
 return 0;
}