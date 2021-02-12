#include<stdio.h>
#include <stdlib.h>

int main()
{
    char word[101][101],word2[101][101], dec[100];
    int i,j,n,length;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        scanf("%s[^\n]",word[i]);
    }
    for(i=0;i<n;i++)
    {
       length=strlen(word[i]);
       if(length>10)
       {
           word2[i][0]=word[i][0];
           itoa(length-2,dec,10);
           if(length-2==9)
           {
               word2[i][1]=dec[0];
               word2[i][2]=word[i][length-1];
               word2[i][3]='\0';
           }
           else if(length-2>9){
                word2[i][1]=dec[0];
                word2[i][2]=dec[1];
                word2[i][3]=word[i][length-1];
                word2[i][4]='\0';
           }

       }
       else
       {
           strcpy(word2[i],word[i]);
       }
    }
    for(i=0;i<n;i++)
    {
       puts(word2[i]);
    }


    return 0;
}
