#include <stdio.h>

int main()
{
    int n , a , b , c , d , s , r , i=0 , rank=1 ;
    scanf("%d",&n);
    scanf("%d%d%d%d",&a,&b,&c,&d);
    s = a + b + c +d;
    for(i=1;i<n;i++){
        scanf("%d%d%d%d",&a,&b,&c,&d);
        r = a + b + c + d;
        if(r>s){
            rank++;
        }
    }
    //printf("%d",rank);
    printf("%d",rank);
    
    
}
