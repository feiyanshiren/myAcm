#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
struct T
{
int a,b;
}c[10010];
int cmp(T n,T m)
{
if(n.a<m.a)
return 1;
if(n.a==m.a && n.b>m.b)
return 1;
return 0;
}
int main()
{
int i,m,n,k=0;
int w,h,x,r;
scanf("%d",&m);
while(m--)
{int k=0; int max=-1;
scanf("%d %d %d",&n,&w,&h);
for(i=0;i<n;i++)
{
scanf("%d %d",&x,&r);
if(2*r>h)
{
c[k].a=x-sqrt(r*r-h*h/4);
if(c[k].a<0)
c[k].a=0;
c[k].b=sqrt(r*r-h*h/4)+x;
if(c[k].b>w)
c[k].b=w;
if(c[k].b>max)
max=c[k].b;
k++;
}
}

sort(c,c+k,cmp);
if(c[0].a!=0 || max!=w)
printf("0\n");
else
{ int count=0;
int f=0;
int start=0,last=0;
while(start!=w)
{
for(i=f; i<k; i++)
if(c[i].a<=start && c[i].b>last)
{
last=c[i].b;
f=i+1;
}
if(last==start)
{
count=0;
break;
}
start=last;
count++;
}
cout<<count<<endl;
}
}
return 0;
}