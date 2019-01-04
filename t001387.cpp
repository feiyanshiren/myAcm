#include <iostream> 
#include <math.h> 
using namespace std; 

bool isPerfectSquare(long long x) 
{ 
	long long s = sqrt(x); 
	return (s*s == x); 
} 

bool isFibonacci(long long n) 
{ 
	return isPerfectSquare(5*n*n + 4) || 
		isPerfectSquare(5*n*n - 4); 
} 


int main(int argc, char **argv)
{
        long long  n;
        while(1){
                scanf("%lld", &n);
                if(0 == n) break;
                (isFibonacci(n))?printf("YES\n"):printf("NO\n");
 
        }
 
        return 0;
}

