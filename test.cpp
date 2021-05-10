#include "stdio.h"
int main(int argc, char const *argv[])
{
    /* code */
    int j = 0;
    for(int i = 0; i < 1000000; i++)
    {
        j = i;
    }
    printf("%d", j);
    return 0;
}
