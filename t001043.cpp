#include<stdio.h>
#include<math.h>
int main()
{
int n;
double a,b;
scanf("%d",&n);
double f(double );
while(n--)
{
scanf("%lf %lf",&a,&b);
printf("%.0f\n",f(b)-f(a));
}
return 0;
}
double f(double x)
{
double s;
if(x>=0&&x<=2)
s=4.0/3*pow(x,1.5)-0.4*pow(x,2.5)+288.741504;
else if(x>2&&x<=5)
s=0.25*pow(x,4)-2.0/3*pow(x,3)-0.5*pow(x,2)+2*x+289.583332;
else if(x>5&&x<=10)
s=72*x-8.0/15*pow(x-5,1.875);
return s;
}