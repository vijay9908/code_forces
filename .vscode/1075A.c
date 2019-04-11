#include <stdio.h>

int main(){
    long long int n , x , y ;
    scanf("%lld",&n);
    scanf("%lld%lld",&x,&y);
    if(x+y-1 <= n){
        printf("White");
    }
    else
    {
        printf("Black");
    }
    return 0 ;
}
