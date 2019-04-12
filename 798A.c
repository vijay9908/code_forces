#include <stdio.h>
#include <string.h>

int main(){
    char a[100];
    int n , i , count=0;
    scanf("%s",a);
    n = strlen(a);
    for(i=0;i<n/2;i++){
        if(a[i]!=a[n-i-1]){
            count++;
        }
    }
    if(count==1 || (count==0 && n%2!=0)){
        printf("YES");
    }
    else{
        printf("NO");
    }
}