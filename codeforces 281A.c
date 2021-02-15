    #include <stdio.h>
    #include <string.h>
    #include<ctype.h>

    int main()
    {
        char a[1001];
        char b;
        scanf("%s",a);
        b=a[0];
        b=toupper(b);
        a[0]=b;
        printf("%s",a);

        return 0;
    }
