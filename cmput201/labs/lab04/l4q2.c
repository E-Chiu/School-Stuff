/*
cmput 201 l4q2
Date: Sept 25, 2020
Refrences: None
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

int main(){
	int col = 5;
	int row = 3;
	char grid[row][col];
	// get user input
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {	
			scanf("%c", &grid[i][j]);
		}
	}
	// print out pyramid
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
		printf("%c", grid[i][j]);
		}
		printf("\n");
	}
	char key = grid[2][1]; // get the character that makes the pyramid
	printf("%c", key);
	int pyramid = 1;
	for (int i = 1; i < col -1; i++) { // check if values in row 2 correspond to key
		if (grid[1][i] != key) {
			pyramid = 0;
		}
	}
	for (int i = 0; i < col; i++) { // check bottom row
		if(grid[2][i] != key) {
			pyramid = 0;
		}
	}
	if (grid[0][0] != key || grid[0][1] != key || grid[0][3] != key || grid[0][4] != key || grid[1][0] != key || grid[1][4] != key) {
		// hardcode checks for the other spots becuase I can't think of a better way
		pyramid = 0;
	}
	// declare whether or not it is a pyramid
	if(pyramid) {
		printf("This is a pyramid");
	} else {
		printf("This is not a pyramid");
	}
}
