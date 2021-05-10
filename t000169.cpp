
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int prim[1010];
void is_prim()
{
	int i,j;
	for(i=2;i<=sqrt(1010);i++)
	{
		if(!prim[i])
		{
			for(j=i*i;j<1010;j+=i)
			{
				prim[j]=1;
			}
		}
	}
	prim[1]=1;
}
int main()
{
	int m,n,i,j;
	scanf("%d",&m);
	is_prim();
	while(m--)
	{
		scanf("%d",&n);
		for(i=0;;i++)
		{
			if(!prim[n+i])
			{
				printf("%d\n",n+i);
				break;
			}
			if(!prim[n-i])
			{
				printf("%d\n",n-i);
				break;
			}
		}
	}
	return 0;
}