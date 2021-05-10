#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int c;
long long a[1000000];
int main()
{
    long long n, m;
    c = 0;
    a[c++] = 1;
    a[c++] = 7;
    int k = 0;
    while (a[c - 1] <= 1e18)
    {
        a[c++] = a[k] * 10 + 1;
        a[c++] = a[k] * 10 + 7;
        k++;
    }
    while (cin >> n >> m)
    {

        int count = 0;
        for (int i = 0; i < c; i++)
        {
            if (a[i] >= n && a[i] <= m)
            {

                count++;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}
