/*
cmput 201 l4q1
Date: Sept 25, 2020,
Refrences: My old code
Lab Session: D01
Name : Ethan Chiu
*/

#include <stdio.h>
void bubbleSort(int toSort[], int size) {
	// sorts given array by "bubbling up" values
	int temp;
	for (int i = size -1 ; i < size; i--) {
		for (int j = 0; j < size - 1; j++) {
			// find if next element is bigger and swap if it is
			if(toSort[j] > toSort[j + 1]) {
			temp = toSort[j + 1];
			toSort[j + 1] = toSort[j];
			toSort[j] = temp;
			}
		}
	}
}

int binarySearch(int list[], int toFind, int min, int max, int half) {
	// searches for value by splitting sorted array into halves
	if (list[half] == toFind) { // check if its the right value
		return half;
	} else if (max <= min) { // return -1 if not found
		return -1;
	} else if (list[half] < toFind) { // if half is lower than toFind search top half
		min = half;
		half = (max + min) / 2;
		return binarySearch(list, toFind, min, max, half);
	} else if (list[half] > toFind) { // if half is higher than toFind search lower half
		max = half;
		half = (max + min) / 2;
		return binarySearch(list, toFind, min, max, half);
	}
}

int main() {
	int size;
	printf("Enter the length of the array: "); // ask user for input
	scanf("%d", &size);
	int toSort[size];
	printf("Enter %d integers to be sorted: ", size); // loop until all values are recieved
	for (int i = 0; i < size; i++) {
		scanf("%d", &toSort[i]);
	}
	// sort given array using bubble sort
	bubbleSort(toSort, size);
	// print results
	printf("In sorted non-decreasing order: ");
	for (int i = 0; i < size; i++) {
	printf("%d ", toSort[i]);
	}
	// ask user what number they want to find
	int toFind;
	printf("\nEnter the integer you wish to locate: ");
	scanf("%d", &toFind);
	// find number with binary search
	int index = binarySearch(toSort, toFind, 0, size - 1, size / 2);
	printf("It's found at position/index: %d\n", index);
}