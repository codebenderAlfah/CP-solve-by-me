#include<Stdio.h>

int main()
{
    int n,i,j;
    int temp=0,val=0;
    int a[999][3];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        temp=0;
        for(j=0;j<3;j++)
        {
            scanf("%d",&a[i][j]);
            if(a[i][j]==1)
            {
                temp++;
            }
        }
        if(temp>=2)
        {
            val++;
        }
    }
    printf("%d",val);
    return 0;
}
