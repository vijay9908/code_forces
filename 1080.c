
By vijay9908, contest: Codeforces Round #524 (Div. 2), problem: (A) Petya and Origami, Accepted, #
 #include <stdio.h>

int main()
{
    int r=2 , g=5 , b=8 , k , n ;
    scanf("%d%d",&n,&k);
    r = r*n;
    g = g*n;
    b = b*n;
    if(r%k != 0){
        r = (r/k) + 1;
    }
    else{
        r = r/k;
    }
    if(g%k != 0){
        g = (g/k) + 1;
    }
    else{
        g = g/k;
    }
    if(b%k != 0){
        b = (b/k) + 1;
    }
    else{
        b = b/k ;
    }
    printf("%d",r+g+b);
}
