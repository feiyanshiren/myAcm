#include <stdio.h>
main(){
    int a1, b1, c1, a2, b2, c2, a, s1, s2;
    while(1){
       a = scanf("%d", &a1);
       if(a == EOF){
           break;
       }
       scanf("%d", &b1); 
       scanf("%d", &c1); 
       scanf("%d", &a2); 
       scanf("%d", &b2); 
       scanf("%d", &c2);
       if(c1 < 90 && c2 < 90){
           printf("-1\n");
       }
       else if(c1 < 90 && c2 >= 90){
           printf("2\n");
       }
       else if(c1 >= 90 && c2 < 90){
           printf("1\n");
       }
       else{
           s1 = a1 + b1 + c1;
           s2 = a2 + b2 + c2;
           if(s1 >= s2){
               printf("1\n");
           }
           else{
               printf("2\n");
           }
       }
    }
}
