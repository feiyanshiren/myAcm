#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int num[1010],arr[1010],len;
int finds(int i){
    int l=0,r=len,mid;
    while(l<r){
        mid=l+(r-l)/2;
        if(arr[mid]>num[i]){
            r=mid;
        }else{
            l=mid+1;
        }
    }
    return l;
}
int main(){
    int t,n,m,i,s;
    scanf("%d",&t);
    while(t--){
        memset(num,0,sizeof (num));
        memset(arr,0,sizeof (arr));
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",&num[i]);
        }
        arr[len=0]=num[0];
        for(i=1;i<n;i++){
            if(num[i]>arr[len]){
                arr[++len]=num[i];
            }else{
                s=finds(i);
                arr[s]=num[i];
            }
 
        }
        printf("%d\n",n-len-1);
    }
    return 0;
}