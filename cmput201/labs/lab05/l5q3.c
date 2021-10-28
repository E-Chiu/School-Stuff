/*
cmput 201 l5q3
Date: Oct 1, 2020
Refrences: devdocs.io/c/
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void initialization(int n, int matrix[n][n]) {
	// initialize n x n array and fill with 1s and 0s
	srand(time(NULL)); // use time as seed for random
	// initialize matrix to have all 0s
	for (int i = 0; i < n; i++) {
		for (int j  = 0; j < n; j++) {
			matrix[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) { // choose n/2 random indexes per row to put a 1
		int put = 0;
		while (put < n/2) {
			int rIndex = rand() % n;
			if (matrix[i][rIndex] != 1) { // enter 1 into index if not already 1
				matrix[i][rIndex] = 1;
				put++;
			}
		}
	}
}

void swap(int row, int i1, int i2, int n, int matrix[n][n]) {
	// swap given indexes in given row of given matrix
	int temp;
	temp = matrix[row][i1];
	matrix[row][i1] = matrix[row][i2];
	matrix[row][i2] = temp;
}

int count1s (int n, int matrix[n][n], int col) {
	// returns # of 1s in a column
	int count = 0;	
	for (int j = 0; j < n; j++) {
		if (matrix[j][col] == 1) {
			count++;
		}
	}
	return count;
}

void balance1(int n, int matrix[n][n]) {
	int count = 0;
	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) {
			count = count1s(n, matrix, col); // count # of 1s in column
			if (count > n/2) { // if too many 1s
				for (int j = 0; j < n; j++) {
					if (count1s(n, matrix, j) < n/2) { // find next available free column
						swap(row, col, j, n, matrix);
					}
				}
			}
		}
	}
}

int main() {
	int n;
	printf("Enter the size of a matrix, a positive even integer: ");
	scanf("%d", &n);
	// ensure valid input
	if (n < 2 || n > 80 || (n % 2) != 0) {
		exit(0);
	}
	int matrix[n][n]; //  declare matrix
	initialization(n, matrix); // initialize matrix
	// print out matrix
	printf("Initial %dx%d matrix:\n", n, n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d", matrix[i][j]);
		}
		printf("\n");
	}
	balance1(n, matrix); // balance 1s
	// print out final matrix
	printf("Final balanced matrix:\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d", matrix[i][j]);
		}
		printf("\n");
	}
	return 0;
}

