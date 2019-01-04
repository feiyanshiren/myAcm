#include <stdio.h>
#include <math.h>
#include <string.h>
bool isPrime(unsigned long n) {
    if (n <= 3) {
        return n > 1;
    } else if (n % 2 == 0 || n % 3 == 0) {
        return false;
    } else {
        for (unsigned short i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

int main()
{
    int n;
    int z;
    int a[10001];
    int b[10001];
    int i;

    while (scanf("%d", &n) != EOF)
    {
        z = 0;
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        for(i=0; i<n; i++)
        {
            a[i] = i + 1;
        }
        for(i=0; i<n; i++)
        {
            b[i] = n - i;
        }
        for(i=0; i<n; i++)
        {
            if(isPrime(a[i]) && isPrime(b[i]))
            {
                z++;
            }
        }
        printf("%d\n", z);
    }
}