#include<stdio.h>
#include<string.h>

int main()
{
    int i,t;
    char a[300];
    scanf("%s",a);
    for(i=0;i<strlen(a);i++)
    {
        if(a[i]!='a'&&a[i]!='e'&&a[i]!='i'&&a[i]!='o'&a[i]!='u'&&a[i]!='n')
        {
            if(a[i+1]=='a'||a[i+1]=='e'||a[i+1]=='i'||a[i+1]=='o'||a[i+1]=='u')
            {
                t=1;
            }
            else
            {
                t=0;
                break;
            }
        }
        else
        {
            t=1;
        }
    }
    if(t == 1)
    {
        printf("YES");
    }
    else if(t == 0)
    {
        printf("NO");
    }
}