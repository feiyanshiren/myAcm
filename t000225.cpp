
#include<stdio.h>
int fun(int x)
{
	int i;
	for(i=2;i<x;i++)
	if(x%i==0)   return 0;
	return 1;
}
int main()
{
	int n;
	scanf("%d",&n); 
	while(n--)
	{
		int m,i;
		long long sum=1;
		scanf("%d",&m);
		for(i=2;i<=m;i++)
		{
			if(fun(i))
			sum=sum*i%1000000;
		}
		printf("%lld\n",sum);
	} 
	return 0;
}