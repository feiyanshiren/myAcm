#include <stdio.h>
int main()
{
	long long t,a,b,sum1,sum2,j,i;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld %lld",&a,&b);
		if(a-b<b)
		b=a-b;
		sum1=sum2=1;
		for(j=a,i=1;i<=b;i++,j--)
		{
			if(j%i==0||sum1%i==0)
			{
				sum1=sum1*j/i;
				continue;
			}		
			if(sum1%sum2==0)
			sum1=sum1/sum2,sum2=1;
			sum1=sum1*j;
			sum2=sum2*i;
		}
		printf("%lld\n",sum1/sum2);
	}
	return 0;
}
