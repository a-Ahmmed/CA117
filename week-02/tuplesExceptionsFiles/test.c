#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char*argv[])
{
    for(int i = 0; i < 10; ++i)
    {
       printf("Test\n");
       sleep(2);
    }

    return 0;
}
