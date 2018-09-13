#include<stdio.h>  
#include<string.h>  
#include<string>  
#include<iostream>  
using namespace std;  
int num[10000];  
string a[10000];  
int vis[10000];  
int cmp(string a,string b)  
{  
    string c;  
    for(int i=0; i<a.length(); i++)  
    {  
        if(a[i]=='('||a[i]==')')  
        {  
            if(c==b)  
                return 1;  
            c.clear();  
        }  
        else c+=a[i];  
    }  
    if(c==b)  
        return 1;  
    return 0;  
}  
int main()  
{  
    string b;  
    string s;  
    string ans;  
    memset(num,0,sizeof(num));  
    int t;  
    scanf("%d",&t);  
    getchar();  
    for(int i=1; i<=t; i++)  
    {  
        getline(cin,s);  
        getline(cin,a[i]);  
        getline(cin,ans);    
        if(ans[0]=='T')  
            num[i]=1;  
        else if(ans[0]=='F')  
            num[i]=2;  
    }  
    int z;  
    scanf("%d",&z);  
    getchar();  
    for(int i=1; i<=z; i++)  
    {  
        int res=0;  
        for(int j=1; j<=t; j++)  
        {  
            getline(cin,b);  
            string c,d;  
            memset(vis,0,sizeof(vis));  
            if(num[j]==1)  
            {  
                int p,q;  
                p=q=0;  
                int flag=0;  
                while(!flag)  
                {  
                    for(; p<a[j].length(); p++)  
                    {  
                        if(a[j][p]=='|')  
                            break;  
                        c+=a[j][p];  
                    }  
                    p++;  
                    for(; q<b.length(); q++)  
                    {  
                        if(b[q]=='|')  
                            break;  
                        d+=b[q];  
                    }  
                    q++;    
                    if(cmp(c,d))  
                        res++;  
                    c.clear();  
                    d.clear();  
                    int e=a[j].length();  
                    int f=b.length();  
                    if(p>=a[j].length()&&q>=b.length())  
                        flag=1;  
                }  
            }  
            else if(num[j]==2)  
            {  
                int q;  
                q=0;  
                while(q<b.length())  
                {  
                    d.clear();  
                    for(; q<b.length(); q++)  
                    {  
                        if(b[q]=='|')  
                            break;  
                        d+=b[q];  
                    }  
                    q++;  
                    int p=0;  
                    while(p<a[j].length())  
                    {  
                        c.clear();  
                        for(; p<a[j].length(); p++)  
                        {  
                            if(a[j][p]=='|')  
                                break;  
                            c+=a[j][p];  
                        }  
                        p++;  
                        if(vis[p])  
                            continue;  
                        if(cmp(c,d))  
                            res++,vis[p]=1;  
                    }  
                    int aa=b.length();   
                }  
            }  
        }  
        printf("%d\n",res);  
    }  
    return 0;  
}  