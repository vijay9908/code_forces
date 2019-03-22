#include <stdio.h>
#include <string.h>

int main(){
    int n , j=0 , i=0;
    scanf("%d",&n);
    char s[n+1];
    scanf("%s",&s);
    while(i<n){
        printf("%c",s[i]);
        j++;
        i += j;
    }
}
    