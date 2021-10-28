/*
cmput 201 l2q3
refrences: devdocs.io/c
author: Ethan Chiu
*/
#include <stdio.h>

int main() {
	/* initialize variables */
	int windows;
	float price;
	
	printf("How many windows do you have:"); /* ask user for number of windows */
	scanf("%d", &windows);
	price = 8 * windows;
	/* calculate if discount is needed */
	if (windows > 24 && windows < 49) {
		price = price * .95;
	} else if (windows > 49 && windows < 99) {
		price = price * .90;
	} else if (windows > 99 && windows < 499) {
		price = price * .80;
	} else if (windows > 499) {
		price = price * .60;
	}
	price = price + 25; /* add base service fee after discounts */
	printf("Your estimate for window cleaning is: %.1f\n", price);
}
