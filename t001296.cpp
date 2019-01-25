#include <stdio.h>

main(){
    int a1, a2, a3;
    while(1){
        scanf("%d", &a1);
        if(a1 == 0){
            break;
        }
        scanf("%d", &a2);
        scanf("%d", &a3);
        if(a1 == 0 || a2 == 0 || a3 == 0){
            printf("oh,my god!\n");
        }
        else{
            if(a1 + a2 > a3 &&
               a1 + a3 > a2 &&
               a2 + a3 > a1){
                   printf("Great,you are genius!\n");
               }
            else{
                printf("oh,my god!\n");
            }
        }
    }
}
