#include<stdio.h>
#include<string.h>
bool x[100005];
int n,m;
void slove()
{
	int cnt=0;char a[15];
	for(int i=0;i<m;++i)
	{
		scanf("%s",a);
		if(a[0]=='C')
		{
			int b;
			scanf("%d",&b);
			if(x[b]==0)
			{
				++cnt;
			}
			else
			{
				--cnt;
			}
			x[b]=!x[b];
		}
		else
		{
			printf("%d\n",cnt);
		}
	}
}
int main()
{
	while(~scanf("%d%d",&n,&m))
	{
		memset(x,0,sizeof(x));
		slove();
	}
	return 0;
}
