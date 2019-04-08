#include <stdio.h>
#include <string.h>

int main(){
    char a[100];
    scanf("%s",a);
    if(a[0]>91){
        a[0] -= 32 ;
    }
    printf("%s",a);
}