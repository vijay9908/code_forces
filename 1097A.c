#include <stdio.h>
#include <string.h>

int main(){
    char a[100] , b[100];
    int i=0 , m=0 ;
    scanf("%s",&a);
    scanf("%s",&b);
    int k = strlen(b);
    while(k>0){
        if(b[i]==a[0] || b[i]==a[1]){
             m += 1;
        }
        i++;
        k--;
    }
    if(m==1){
        printf("YES");
    }
    else{
        printf("NO");
    }
        
    
}