#include <stdio.h>
#include <math.h>
bool isPrime(unsigned long n) {
    unsigned long f = (unsigned long)sqrt(n);
    unsigned long i;
    for(i = 2; i < f + 1; i++)
    {
        if(n % i == 0)
        {
            return false;
        } 
    }
    return true;
}

int main()
{
    int T;
    int i;
    unsigned long N;
    scanf("%d", &T);
    for(i = 0; i < T; i++)
    {
        scanf("%d", &N);
        if(isPrime(N))
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
        
    }

}