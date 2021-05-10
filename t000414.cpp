#include <stdio.h>
 
int sum(int m ,int n)
{
	int result = 0;
	while (m != 0)
	{
		result += m % n;
		m /= n;
	}
	return result;
}
 
int main()
{
	int m;
	while (~scanf("%d",&m) && m)
	{
		if (sum(m,10) == sum(m,12) && sum(m,10) == sum(m,16))
		{
			printf("%d is a Sky Number.\n",m);
		}
		else
		{
			printf("%d is not a Sky Number.\n",m);
		}
 
	}
	return 0;
}
