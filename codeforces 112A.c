#include<stdio.h>

int main()
{
    int x;
    char a[100],b[100];
    scanf("%s",a);
    scanf("%s",b);
    if(strcmpi(a,b)==0)
    {
        x=0;
        printf("%d",x);
    }
    else if(strcmpi(a,b)==1)
    {
        x=1;
        printf("%d",x);
    }
    else if(strcmpi(a,b)==-1)
    {
        x=-1;
        printf("%d",x);
    }

    return 0;
}
