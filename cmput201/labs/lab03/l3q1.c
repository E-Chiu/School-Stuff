/*
Cmput 201 l3q1
Lab Section: D01
Date: Sept 17, 2020
Refrences: None
Author: Ethan Chiu
*/
#include <stdio.h>

int main() {
	/* using for loop */
	for(int bottles = 99; bottles > 0; bottles--) {
		switch(bottles) {
			case 1:
				printf("%d bottle of beer on the wall,\n%d bottle of beer.\n", bottles, bottles);
				break;
			default:
				printf("%d bottles of beer on the wall,\n%d bottles of beer\n", bottles, bottles);
				break;
		}
		printf("Take one down, pass it around\n");
		printf("%d bottles of beer on the wall.\n\n", bottles - 1);
	}
	/* using while loop */
	int bottles = 99;
	while (bottles > 0) {
		switch(bottles) {
			case 1:
				printf("%d bottle of beer on the wall,\n%d bottle of beer.\n", bottles, bottles);
				break;
			default:
				printf("%d bottles of beer on the wall,\n%d bottles of beer\n", bottles, bottles);
				break;
		}
		printf("Take one down, pass it around\n");
		bottles -= 1;
		printf("%d bottles of beer on the wall.\n\n", bottles);
	}
	/* using do while loop */
	bottles = 99;
	do {
		switch(bottles) {
			case 1:
				printf("%d bottle of beer on the wall,\n%d bottle of beer.\n", bottles, bottles);
				break;
			default:
				printf("%d bottles of beer on the wall,\n%d bottles of beer\n", bottles, bottles);
				break;
		}
		printf("Take one down, pass it around\n");
		bottles -= 1;
		printf("%d bottles of beer on the wall.\n\n", bottles);
	} while (bottles > 0);

}
