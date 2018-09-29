#include <stdio.h>
 
int main()
{
	int n;
	while (~scanf("%d",&n) && (n != -1 ))
	{
		int temp = 1,i;
		for (i=2; i*i<n; i++)
		{
			if (n % i == 0)
			{
				temp += i + n / i;
			}
		}
		if (i*i == n)
		{
			temp += i;
		}
		if (n == 1 || temp != n)
		{
			printf("No");
		}
		else
		{
			printf("%d=1",n);
			for (i=2; i<=n/2; i++)
			{
				if (n % i == 0)
				{
					printf("+%d",i);
				}
			}
		}
		printf("\n");
	}
	return 0;
}
