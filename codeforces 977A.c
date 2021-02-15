    #include <stdio.h>
    #include <string.h>


    int main()
    {
        int b,y=0;
        long int a;
        scanf("%d",&a);
        scanf("%d",&b);
        while(b!=0)
        {
            y=a%10;
            if(y==0)
            {
                a=a/10;
            }
            else
            {
                a=a-1;
            }
            b=b-1;
        }
        printf("%ld",a);
        return 0;
    }
