#include<iostream>//最优codes
#include<cstdio>
using namespace std;
 
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=1;;i++)
        {
            int k=1;
            int s=i;
            while(s)
            {
                k*=(s%10);
                s/=10;
            }
            if(k==n)
            {cout<<i<<endl;break;}
            if(i>5000)
            {cout<<"-1"<<endl;break;}
        }
    }
    return 0;
}