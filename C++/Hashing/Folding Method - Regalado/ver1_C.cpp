#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char string[20],
		 checker;
    int n,
		count = 0,
		sum = 0,
		repeat = 1,
		digits;

		printf("\nFolding Method For C Keywords\n");

    while(repeat == 1){
	    printf("\nEnter the string: ");
	    scanf("%s", string);

	    n = strlen(string);

	    printf("\n");

	    while (count < n)
	    {
	        printf(" %c = %d\n", string[count], string[count] );
	        sum += string[count];
	        ++ count ;
	    }

	    printf("\nsum = %d\n", sum);
	    printf("\nstrlen = %d\n", n);
	    printf("\nhash value (arraysize = 32)= %d\n", sum % 32);

	    printf("\nEnter another string? (Y/N): ");
	    scanf(" %c", &checker);

	    if(checker == 'Y'||checker == 'y')
	    	repeat = 1;
	    else repeat = 0;

	    count = 0;
	    sum = 0;
	}

    return 0;
}
