/*
cmput 201 l5q2
Date: Oct 1, 2020
Refrences: None
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

int fibMod(int num) {
	/* either returns constant number if num = 0,1,2 or
	   the sum of the last 3 numbers in fibonacci sequence */
	switch(num) {
		case 0:
			return 0;
			break;
		case 1:
			return 1;
			break;
		case 2:
			return 2;
			break;
		default:
			return (fibMod(num - 3) + fibMod(num - 2) + fibMod(num - 1));
	}
}

int main() {
	// loop until user enters a invalid number and call fibMod
	int num;
	printf("Enter a position index: "); 
	scanf("%d", &num); // prompt user for input
	while(num >= 0) { // loop while user input is a valid index
		printf("Term %d has a value: %d\n", num, fibMod(num)); // print fibMod
		printf("Enter a position index: ");
		scanf("%d", &num);
	}
	return 0;

}
