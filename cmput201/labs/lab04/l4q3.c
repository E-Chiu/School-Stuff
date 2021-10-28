/*
cmput 201 l4q3
Date: Sept 25, 2020
Refrences: slides, stackoverflow, geeksforgeeks
Lab Section: D01
Name: Ethan Chiu
*/
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main() {
	char input[9999];
	char message[99999];
	printf("Integer conversion in decimal (d), octal (o), or hexadecimal (h)?");
	input [0] = toLower(scanf("%c", input[0]));
	int i = 0;
	while (input[i] != "\n") { // convert input to lowercase
		input[i] = tolower(scanf("%c", &input[i]));
	}
	while (strcmp(input,"exit") != 0) {
		if (strcmp(input,"d") != 0) { //  decimal conversion
			printf("Enter a message: ");
			scanf(" %c", &message[0]);
			int j = 0;
			while(message[j] != "\n") {
				printf("%d ", message[j]);
				j++;
				scanf(" %c", &message[j]);
			}
		} else if (strcmp(input,"o") != 0) { // octal conversion
			printf("Enter a message: ");
			scanf(" %s", message);
			int number;
			int octalNum[100];
			int temp;
			for (int j = 0; j < sizeof(message); j++) {
				number = message[j];
				temp = 0;
				while (number != 0) { // convert character to octal using remainders
					octalNum[temp] = number % 8;
					number = number / 8;
					temp++;
				}
				printf("0"); // add octal prefix
				for(int k = 0; k < temp - 1; k++) { // print octal number
				printf("%d", octalNum[k]);
				}
				printf(" ");
			}
		} else if (strcmp(input,"h") != 0) { // hexadecimal conversion
				printf("Enter a message: ");
				scanf(" %s", message);
				for (int j = 0; j < sizeof(message); j++) {
				printf("0x%x ", message[j]);
			}
		}
	}
}
