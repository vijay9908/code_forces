#include <stdio.h>

int main(){
    int t , i , s , a , b , c , q , w ;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d%d%d%d",&s,&a,&b,&c);
        printf("%d",s/c/a*b + s/c); 
    }
}