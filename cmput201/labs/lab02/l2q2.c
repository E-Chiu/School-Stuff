/*
cmput 201 l2q2
refrences: devdocs.io/c
author: Ethan Chiu
*/

#include <stdio.h>

int subtract(int* dollars, int amount) {
	/* returns how much of amount can go into bills */
	int total = *dollars;
	int left = total % amount; 
	int times = (total - left) / amount;
	*dollars = left;
	return times;
}

int main() {
	/* main function for program */
	int dollars, times = 0;
	int amounts[4] = {100, 20, 2, 1};
	char names[4][11] = {"$100 bills", "$20 bills", "toonies", "loonies"};

	printf("Enter a dollar amount:");
	scanf("%d", &dollars); /* get total amount from user */

	for(int i = 0; i < 4; i++) {
		times = subtract(&dollars, amounts[i]);
		printf("%10s: %d\n", names[i], times);
	}
	
	return 0;
}
