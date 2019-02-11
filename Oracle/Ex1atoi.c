#include <stdio.h>
#include <assert.h>
#include <ctype.h>

int my_atoi(const char *c)
{


   int value = 0;
    int sign = 1;

    while (isdigit(*c))
    {


        value *= 10;
        value += (int) (*c-'0');


        c++;
    }


    return (value * sign);
}




int main(void)
{

  //4 byte -32,768 to 32,767
    //test1
   assert(5 == my_atoi("5"));

   //Test2
    assert(-2 == my_atoi("-2"));

    //print("Finish.");
}
