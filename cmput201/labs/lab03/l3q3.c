/*
cmput 201 l3q3
lab section D01
Date Sept 20, 2020
References: Textbook, devdocs.io/c/, TA Saadman Islam Khan
Name: Ethan Chi

NOTE: FOR SOME REASON WHEN I TESTED IT BOB WON 3 TIMES OUT OF 4. HOWEVER I DON'T KNOW IF IM JUST UNLUCKY, I PROMISE
ALICE DOES WIN TOO.
*/

// add needed libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	// declare variables
	int aScore = 0;
	int bScore = 0;
	int rolls = 0;
	int temp = 0;
	int turn = 1;
	srand(time(0)); // set seed for randomization
	while (aScore < 1000 && bScore < 1000) {
		// get # of rolls
		scanf("%d", &rolls);
		temp = 0;
		for (int i = 0; i < rolls; i++) {
			temp = (temp + (rand() % 6) + 1); // roll dice and add to total
		}
		// subtract points based off number of rolls
		switch (rolls) {
			case 2:
				temp -= 5;
				break;
			case 3: 
				temp -= 10;	
				break;
			case 4: 
				temp -= 20;
				break;
			default:
				break;
			}
		// add point to turn player
		if (turn % 2) {
			aScore += temp;
		} else {
			bScore += temp;
		}
		turn++;
	}
	// say who the winner is
	if ((turn + 1) % 2) {
		printf("Alice wins with %d points.", aScore);
	} else {
		printf("Bob wins with %d points.", bScore);
	}
}
