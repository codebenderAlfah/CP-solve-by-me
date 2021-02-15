    #include <stdio.h>
    #include <string.h>


    int main()
    {
        char names[101];
        char temp[101];
        int i,j,x,count=0,res;
        scanf("%s",names);
        strcpy(temp,names);
        x=strlen(names);
        for(i=0;i<x;i++)
        {
            for(j=i+1;j<x;j++)
            {
                if(temp[i]==names[j])
                {
                    count++;
                    names[j]='*';
                }
            }
        }
        res=x-count;
        if(res%2!=0)
        {
            printf("IGNORE HIM!");
        }
        else
        {
            printf("CHAT WITH HER!");
        }
        return 0;
    }
