#include <stdio.h>

int main(){
    int n , i , ch = 0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    while(ch<n-1 && (a[ch]<a[ch+1])){
        ch++;
    }
    while(ch<n-1 && a[ch]==a[ch+1]){
        ch++;
    }
    while(ch<n-1 && a[ch]>a[ch+1]){
        ch++;
    }
    
    ch++;
    if(ch!=n){
        printf("NO");
    }
    else
    {
        printf("YES");
    }
    

}