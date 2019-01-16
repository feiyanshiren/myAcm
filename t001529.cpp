#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
const int Mod=1e9;
const int INF=0x3f3f3f3f;

const int N=2e3+10;
char a[N][3];
char s1[N];
char ans[N];
int n;

void shuru()
{
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%s",a[i]);
    for(int i=0;i<n;i++)
        s1[i]=a[i][0];
    s1[n]='\0';
}

int main()
{
    shuru();
    int s,t,num;
    s=0;
    t=n-1;
    num=0;
    while(s<=t)
    {
        if(s1[s]==s1[t])
        {
            printf("%c",s1[s]);
            int i,j;
            i=s;
            j=t;
            while(s1[i]==s1[j])
            {
                i++;
                j--;
            }
            if(s1[i]>s1[j])
                t--;
            else
                s++;
        }
        else
        {
            if(s1[s]>s1[t])
            {
                printf("%c",s1[t]);
                t--;
            }
            else
            {
                printf("%c",s1[s]);
                s++;
            }
        }
        num++;
        if(num==80)
        {
            num=0;
            puts("");
        }
    }
}
