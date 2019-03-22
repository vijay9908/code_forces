#include<stdio.h>

int main(){
    long long t,n,num,r=1;
    scanf("%I64d",&n);
    num=n;
    while(num!=0){
        if(num%r!=0){
        break;
        }
        else r*=3;
        }
    t=num/r+1;
    printf("%I64d",t);
}