#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char s[1001][61];

int cp(const void *a, const void * b){
    char c[122],d[122];
    strcpy(c,(const char*)a);
    strcpy(c+strlen(c),(const char*)b);
    strcpy(d,(const char*)b);
    strcpy(d+strlen(d),(const char*)a);
    return strcmp((const char*)c,(const char*)d);
}

int main(void){
    int T;
    scanf("%d\n",&T);
    for(int i,j;T--;){
        for(i = 0;*gets(s[i]);i++);
        qsort(s,i,sizeof(s[0]),cp);
        for (j = i; j>=0; j --)
        {
            printf("%s",s[j]);
        }
        printf("\n");
        for (j = 0; j<i; j ++)
        {
            printf("%s",s[j]);
        }
        printf("\n");
    }
    return 0;
}  
