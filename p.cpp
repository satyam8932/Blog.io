#include<stdio.h>
#include<conio.h>

int main()
{
    int start, end;
    printf("Enter the Start: ");
    scanf("%d",&start);
    printf("Enter the End: ");
    scanf("%d",&end);

    for(int i= start; i<=end; i++)
    {
        if( i%2 == 0 )
        {
            printf("The Even Number is %d : \n",i);
        }
    }
}