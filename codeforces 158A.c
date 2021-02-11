#include<Stdio.h>

int main()
{
    int n,k,i;
    int count=0;
    int a[999];
    scanf("%d %d",&n, &k);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);

    }
    int x=a[k-1];
    if(x!=0)
    {
        count=k;
        for(i=k;i<n;i++)
        {
            if(x<=a[i] && a[i]!=0)
            {
                count++;
            }
        }
    }
    else if(x==0)
    {
        for(i=0;i<n;i++)
        {
            if(x<=a[i] && a[i]!=0)
            {
                count++;
            }
        }
    }
    printf("%d",count);
    return 0;
}

