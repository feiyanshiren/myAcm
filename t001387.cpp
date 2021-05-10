#include<iostream>  
using namespace std;
int main(){
    unsigned __int64 f1=1,f2=1,t,n=1;
    unsigned __int64 a[198];
    cout<<"f1:"<<f1<<endl;
    cout<<"f2:"<<f2<<endl;
    a[0] = f1;
    a[1] = f2; 
    for(n=2;n<100;n++){
    	f1=f1+f2;
        a[2*n-2] = f1;
	cout<<"f"<<(2*n-1)<<":"<<f1<<endl;
	f2=f1+f2;
        a[2*n-1] = f2;
	cout<<"f"<<(2*n)<<":"<<f2<<endl; 
    }	 
	cout<<endl;
        getchar();
	return 0;
}
