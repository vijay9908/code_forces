#include <stdio.h>
#include <math.h>

int main(){
    int m , n , k;
    scanf("%d %d",&n,&m);
    k = n;
    while(k<m){
        if(m%(2*k)==0 && n!=m){
        k = k*2;
        count = count + 1;
        }
    else if(m%(3*k)==0){
        k *=3;
        count = count + 1;
    }
    else{
        if(m<(2*n)){
            count = count - 1;
            break;
        }
    }
    }
    printf("%d",count);
}