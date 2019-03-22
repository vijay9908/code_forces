#include <stdio.h>

int main()
{
    int n , w , h , q=0 , i=1 , s=0;
    scanf("%d%d%d",&w,&h,&q);
    for(i=1;i<=q;i++){
        s += 2*(w+h)-4;
        w -= 4;
        h -= 4;
    }
    printf("%d",s);
}
