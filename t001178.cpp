
#include <stdio.h>
#include <math.h>
int main()
{
	int n;
	float v0,v1,a0,a1,x,t,a,b,dert,x1,x0;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%f %f %f %f %f",&v0,&a0,&v1,&a1,&x);
		if(x==0)
		{
			printf("0.00\n");
			continue;
		}
		if(v0<=v1&&a0<=a1)
		{
			printf("Drong is strong.\n");
			continue;
		}
		if(v0<v1&&a0>a1||v0>v1&&a0>=a1||v0==v1&&a0>a1)
		{
			a=0.5*a0-0.5*a1,b=v0-v1;
			dert=sqrt(b*b+4*a*x);
			t=(-b+dert)/(2*a);
			printf("%.2f\n",t);
			continue;
		}
		if(v0>v1&&a0<a1)
		{
			t=(v0-v1)/(a1-a0);
			x0=v0*t+0.5*a0*t*t;
			x1=v1*t+0.5*a1*t*t;
			if(x0==x1+x)
				printf("%.2f\n",t);
			else if(x0>x1+x)
			{
				a=0.5*a0-0.5*a1,b=v0-v1;
			    dert=sqrt(b*b+4*a*x);
			    t=(-b+dert)/(2*a);
			    printf("%.2f\n",t);
			}
			else
				printf("Drong is strong.\n");
		}
	}
	return 0;
}      