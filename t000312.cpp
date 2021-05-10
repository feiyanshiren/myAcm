
#include <stdio.h>
int main()
{
	int year,mon,day,sum1,sum2,sum3,t,i,flag1,flag2;
	scanf("%d",&t);
	while(t--)
	{
		flag1=flag2=0;
		int a[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};//保存十二个月的天数，2月先用平年计算
		scanf("%d-%d-%d",&year,&mon,&day);
                sum1=sum2=sum3=0;
		for(i=year+1;i<year+20;i++)
		{
			if(i%4==0&&i%100!=0||i%400==0)
				sum1+=366;
			else
				sum1+=365;
		}//计算出生下一年到20岁那年的天数
		if(year%4==0&&year%100!=0||year%400==0)
			a[2]=29,flag1=1;//如果出生那年为闰年2月要修改为29天，并且标记flag1=1;
		for(i=mon+1;i<13;i++)
			sum2=sum2+a[i];
		sum2=sum2+a[mon]-day;//计算出生那年到下一年的天数
		a[2]=28;
		if((year+20)%4==0&&(year+20)%100!=0||(year+20)%400==0)
			a[2]=29,flag2=1;//如果二十岁生日那年为闰年flag2=1;
		for(i=1;i<mon;i++)
			sum3=sum3+a[i];
		if(flag1&&!flag2&&mon==2&&day==29)
			printf("-1\n");//如果出生那年为闰年且为2月29日， 如果year+20不是闰年，那么这个人没有20岁生日。
		else
		printf("%d\n",sum1+sum2+sum3+day);
	}
	return 0;
}   