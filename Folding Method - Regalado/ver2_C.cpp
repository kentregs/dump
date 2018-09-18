#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void FoldingMethod(const char *array[]) {

	int arraysize = 64, //total number of c keywords doubled (original arraysize is 32 since there are 32 c keywords)
			n,
			count = 0,
			sum = 0,
			i,
			j,
			collisions = 0,
			hashVal[32], //int array where the keywords' hashVals are stored for reference
			divisor; //divisor to be used in the Prime Division method

	//this while loop iterates through all the 32 c keywords
	while(count != 32){
		//gets the current keyword's string length
		n = strlen(array[count]);

		/*This entire for loop converts the keyword(character string) into
			an integer sum. Since all keywords only have lowercase letters,
			I've assigned their num to increment in accordance with their
			index in the alphabet added by 1 so that it starts at 1(a) and ends
			at 26(z). Additionally, I've also added a multiplier. Depending on
			the character's index within the keyword, its current sum is multiplied
			by n which ranges from 0 to 8 since 8 is the max string length among
			all the c keywords (continue has 8 as its string length).
		*/
		for(i = 0; i < n; i++){
				if(array[count][i] == 'a'){
					sum += 1;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'b'){
					sum += 2;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'c'){
					sum += 3;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'd'){
					sum += 4;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'e'){
					sum += 5;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'f'){
					sum += 6;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'g'){
					sum += 7;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'h'){
					sum += 8;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'i'){
					sum += 9;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'j'){
					sum += 10;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'k'){
					sum += 11;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'l'){
					sum += 12;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'm'){
					sum += 13;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'n'){
					sum += 14;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'o'){
					sum += 15;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'p'){
					sum += 16;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'q'){
					sum += 17;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'r'){
					sum += 18;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 's'){
					sum += 19;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 't'){
					sum += 20;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'u'){
					sum += 21;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'v'){
					sum += 22;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'w'){
					sum += 23;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'x'){
					sum += 24;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'y'){
					sum += 25;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
				else if(array[count][i] == 'z'){
					sum += 26;

					if(i == 0)
						sum *= 1;
					else if(i == 1)
						sum *= 2;
					else if(i == 2)
						sum *= 3;
					else if(i == 3)
						sum *= 4;
					else if(i == 4)
						sum *= 5;
					else if(i == 5)
						sum *= 6;
					else if(i == 6)
						sum *= 7;
					else if(i == 7)
						sum *= 8;
				}
			//after it finishes converting the entire keyword, the sum is generated.
			if(i == n-1){
				divisor = 61; //greatest prime number before 64(doubled arraysize)
				hashVal[count] = sum % divisor; //generates hashVal through Prime Division method

				//prints the generated hashVal of the current keyword
				printf("[%d] Hash value of %s is = %d\n", count, array[count], hashVal[count]);
			}
		}
		/*for loop that checks if the latest generated hashVal has an equivalent hashVal with
			any of the 31 other keywords.
		*/
		for(j = 0; j < 32; j++){ //iterates through the 32 keys that may or may not have any hashVals yet
			//if current hashVal is equal to any hashVal and their index is not the same, then a collision has occurred
			if(hashVal[count] == hashVal[j] && count != j){
				collisions++;
			}
		}
		//sum is reset to 0 since the while loop will start from the top/start with the next keyword
		sum = 0;
		/*count is incremented in order to iterate through every keyword in the array
			(This while loop will loop a total of 32 times since there are 32 c keywords)
		*/
		count++;
	}
	//prints the number of collisions detected
	printf("\ncollisions = %d\n", collisions);
}

int main()
{
	const char *array[32]; //c keywords are instantiated in a character array
		array[0] = "auto";
		array[1] = "double";
		array[2] = "int";
		array[3] = "struct";
		array[4] = "break";
		array[5] = "else";
		array[6] = "long";
		array[7] = "switch";
		array[8] = "case";
		array[9] = "enum";
		array[10] = "register";
		array[11] = "typedef";
		array[12] = "char";
		array[13] = "extern";
		array[14] = "return";
		array[15] = "union";
		array[16] = "const";
		array[17] = "float";
		array[18] = "short";
		array[19] = "unsigned";
		array[20] = "continue";
		array[21] = "for";
		array[22] = "signed";
		array[23] = "void";
		array[24] = "default";
		array[25] = "goto";
		array[26] = "sizeof";
		array[27] = "volatile";
		array[28] = "do";
		array[29] = "if";
		array[30] = "static";
		array[31] = "while";

		int choice;
		char option = 'y';

		do{
		printf("\n ~ HASH FUNCTIONS FOR C: ~ \n\n");
		printf("[1] - Prime Division Method\n");
		printf("[2] - Digit Exraction Method\n");
		printf("[3] - Folding Method\n\n");

		printf("Please pick a Hash Function you want to use: ");
		scanf("%d", &choice);

		if(choice == 1){
			//insert function call for Prime Division Method here
			printf("\nWould you like to use another method? (Y/N): ");
			scanf(" %c", &option);
		}
		else if(choice == 2){
			//insert function call for Digit Exraction Method here
			printf("\nWould you like to use another method? (Y/N): ");
			scanf(" %c", &option);
		}
		else if(choice == 3){
			printf("\nYou have selected [3] - Folding Method\n\n");
			FoldingMethod(array); //function call for Folding method
			printf("\nWould you like to use another method? (Y/N): ");
			scanf(" %c", &option);
		}
		else{
			do{
				printf("\nInvalid input. Please select only among the 3 choices provided: ");
				scanf("%d", &choice);

				if(choice == 1){
					//insert function call for Prime Division Method here
					printf("\nWould you like to use another method? (Y/N): ");
					scanf(" %c", &option);
				}
				else if(choice == 2){
					//insert function call for Digit Exraction Method here
					printf("\nWould you like to use another method? (Y/N): ");
					scanf(" %c", &option);
				}
				else if(choice == 3){
					printf("\nYou have selected [3] - Folding Method\n\n");
					FoldingMethod(array); //function call for Folding method
					printf("\nWould you like to use another method? (Y/N): ");
					scanf(" %c", &option);
				}
			}while(choice < 1 || choice > 3);
		}
	}while(option == 'Y' || option == 'y');

    return 0;
}
