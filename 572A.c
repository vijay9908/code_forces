#include <stdio.h>

int main(){
    int na , nb , k , m , i ;
    scanf("%d%d",&na,&nb);
    scanf("%d%d",&k,&m);
    int a[na] , b[nb];
    for(i=0;i<na;i++){
        scanf("%d",a[i]);
    }
    i=0;
    for(i=0;i<nb;i++){
        scanf("%d",b[i]);
    }
    if(a[k-1]<b[nb-m]){
        printf("YES");
    }
    else{
        printf("NO");
    }
    
}


