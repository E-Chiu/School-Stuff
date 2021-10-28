/* 
Cmput 201 l3q2
Lab Section: D01
Date: Sept 18, 2020
Refrences: Textbook
Author: Ethan Chiu
*/

#include <stdio.h>

int sortArr(int numbers[20]) {
	/* Just doing insertion sort 
	because I forgot how to do quick */
	int insertVal, insertInd, sourceInd, temp;
	for (int i = 1; i < 20; i++) {
		insertVal = numbers[i];
		sourceInd = insertInd = i;
		/* go through array changing index every time there is a bigger number */
		for (int j = insertInd; j > 0; j--) {
			if (numbers[j - 1] > insertVal) {
				insertInd = j - 1;
			}
		}
		if (insertInd != sourceInd) {
			/* swap values */
			temp = numbers[insertInd];
			numbers[insertInd] = insertVal;
			numbers[sourceInd] = temp;
			i--;
		}
	}
}
int main() {
	int numbers[20] = {}; /* declare numbers array */
	int temp;
	printf("Enter 20 integers:");
	for (int i = 0; i < 20; i++) {
		scanf("%d", &temp);
		numbers[i] = temp;
	}
	sortArr(numbers); /* call function to sort */
	printf("Largest: %d\nSecond largest: %d", numbers[19], numbers[18]);
}
