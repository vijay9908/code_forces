#include <stdio.h>
#include <math.h>

int main()
{
    double n , m , a ;
    long long int req;
    scanf("%lf%lf%lf",&n,&m,&a);
    req = ceil(n/a)*ceil(m/a);
    printf("%I64d",req);
    
}