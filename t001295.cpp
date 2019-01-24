#include <stdlib.h>
#include <stdio.h>
int main(){
    long long d;
    while(1){
        scanf("%lld", &d);
        if(d == 0)
        break;
        printf("%lld\n", llabs(d));
    }
}
