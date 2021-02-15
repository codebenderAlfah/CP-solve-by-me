    #include <stdio.h>
    #include <string.h>


    int main()
    {
        int k,w,i;
        long int n,p=0,b;
        scanf("%d",&k);
        scanf("%d",&n);
        scanf("%d",&w);
        for(i=1;i<=w;i++)
        {
            p=p+(k*i);
        }
        if(n>p)
        {
            printf("0");
        }
        else
        {
            b=abs(p-n);
            printf("%ld",b);
        }

        return 0;
    }
