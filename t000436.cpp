#include<stdio.h>  
#include<math.h>  
  
int SUM(int x) {//递归求解键入负数的处理   
    if(x==2)  
        return 2;  
    return x+SUM(x-1);  
}  
  
int main() {  
    int n,ans;  
    while(scanf("%d",&n)!=EOF) {  
        if(n>0)  
            ans=n*(n+1)/2;  
        else if(n==0)  
            ans=1;  
        else if(n==-1)  
            ans=0;  
        else if(n<=-2) {  
            n=n*(-1);//坑人用 abs()函数运行错误   
            ans=-SUM(n);  
        }  
        printf("%d\n",ans);  
    }  
    return 0;  
}  