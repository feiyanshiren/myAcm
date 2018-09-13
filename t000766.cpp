#include<stdio.h>
int judge(long long int n)
{
	long long int m=n,k=0;
	while(m!=0)
	{
		k=k*10+m%10;//回文数的判断，例：123 等循环结束以后。k=321，
		m/=10;      //比较k和n是否相等即可
	}
	return (k==n);
}
int main()
{
	long long int i,j=0;
	for(i=1;i<=1000000;i++)
	{
		if(judge(i)&&judge(i*i)&&judge(i*i*i))
		{
			printf("%d",i);
			j++;
			if(j%5)
			{
				printf(" ");
			}
			if(j%5==0)
			{
				printf("\n");
			}
		}
	}
	return 0;
}