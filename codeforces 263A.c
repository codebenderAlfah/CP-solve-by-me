#include<stdio.h>

int main()
{
    int i,j,x,y,res;
    int a=2,b=2;
    int mat[5][5];
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            scanf("%d",&mat[i][j]);
            if(mat[i][j]==1)
            {
                x=i;
                y=j;
            }
        }
    }
    a=abs(x-a);
    b=abs(y-b);
    res=abs(a+b);
    printf("%d",res);
    return 0;
}
