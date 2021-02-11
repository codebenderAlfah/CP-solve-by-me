    #include <stdio.h>
    #include <string.h>

    int main()
    {
        int n,x=0,i;
        char stat[150][3];
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",stat[i]);
            if(stat[i][0]=='+' || stat[i][1]=='+' || stat[i][2]=='+')
            {
                x++;
            }
            else if(stat[i][0]=='-' || stat[i][1]=='-' || stat[i][2]=='-')
            {
                x--;
            }
        }
        printf("%d",x);
        return 0;
    }
