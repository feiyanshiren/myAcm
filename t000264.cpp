#include <cstdio>  
#include <cstring>  
#include <iostream>  
using namespace std;  
char str[110];  
  
int change(int len){  
    int i=0,j=len-1;  
    while(i<j){  
        if (str[i]!=str[j])  
            return 0;  
        i++;j--;  
    }  
    return 1;  
}  
  
int main(){  
    int t;  
    cin>>t;  
    while(t--){  
        cin>>str;  
        int len=strlen(str);  
        while(!(len&1) && change(len))  
            len/=2;  
        cout<<len<<endl;  
    }  
    return 0;  
}  
