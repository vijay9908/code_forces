#include <stdio.h>
#include <string.h>

int main(){
    int n , i , j;
    char a[n];
    scanf("%s",a);
    for(i=0;i<n;i++){
        if(a[i]>a[i+1]){
            for(j=i;j<n;j++){
                a[j]=a[j+1];
            }
            break;
        }
    }
    if(strlen(a)==n){
        a[n-1]= ' ';
    }
    printf("%s",a);
}