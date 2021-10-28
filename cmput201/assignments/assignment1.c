/*
cmput201 assignment1
Date: Oct 2, 2020
Refrences: stackoverflow
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
int acceptJobs(int n, int jobArr[n][2]) {
	// randomly accept jobs
	int rejectCost = 0;
	for (int i = 0; i < n; i++) {
		int accept = rand() % 2;
		if (!accept) { //  remove from the array if not accept
			rejectCost += jobArr[i][1];
			jobArr[i][0] = 0;
			jobArr[i][1] = 0;	
		}
	}
	return rejectCost;
}

void sortArr(int n, int arr[n][2]) {
	// sort array in non-descending order
	int insertVal, insertVal2, insertInd, sourceInd, temp, temp2;
	for (int i = 1; i < n; i++) {
		insertVal = arr[i][0];
		insertVal2 = arr[i][1];
		sourceInd = insertInd = i;
		/* go through array changing index every time there is a bigger number */
		for (int j = insertInd; j > 0; j--) {
			if (arr[j - 1][0] > insertVal) {
				insertInd = j - 1;
			}
		}
		if (insertInd != sourceInd) {
			/* swap values */
			temp = arr[insertInd][0];
			temp2 = arr[insertInd][1];
			arr[insertInd][0] = insertVal;
			arr[insertInd][1] = insertVal2;
			arr[sourceInd][0] = temp;
			arr[sourceInd][1] = temp2;
			i--;
		}
	}
}

int findTime(int jobNum, int jobArr[jobNum][2]) {
	// find and return completion time
	int completionTime = 0;
	for (int i = 0; i < jobNum; i++) {
		completionTime += jobArr[i][0];
	}
	return completionTime;
}
 
int main() {
	srand(time(NULL)); // set seed for random
	int jobNum;
	char temp0[9999];
	scanf("%s", temp0); //  get # of jobs to read
	for (int i = 0; i < strlen(temp0); i++) {
		if (!isdigit(temp0[i])) { // terminate program if not a valid input
			printf("Invalid instance");
			exit(0);
		}
	}
	jobNum = atoi(temp0);
	int jobArr[jobNum][2];
	char temp1[9999];
	char temp2[9999];
	for (int i = 0; i < jobNum; i++) {
		scanf("%s%s", temp1, temp2); // get completion time and rejection cost
		for (int j = 0; j < strlen(temp1); j++) {
			if (!isdigit(temp1[j])) { // terminate program if invalid input
				printf("Invalid instance");
				exit(0);
			}
		}
		for (int j = 0; j < strlen(temp2); j++) {
			if (!isdigit(temp2[j])) {
				printf("Invalid instance");
				exit(0);
			}
		}
		jobArr[i][0] = atoi(temp1);
		jobArr[i][1] = atoi(temp2);
	}
	// print input back out
	printf("All Jobs:\n%d\n", jobNum);
	for (int i = 0; i < jobNum; i++) {
		printf("%d %d\n", jobArr[i][0], jobArr[i][1]);
	}
	// calculate objective
	int rejectCost = acceptJobs(jobNum, jobArr);
	int completionTime = findTime(jobNum, jobArr);
	int objective = rejectCost + completionTime;
	sortArr(jobNum, jobArr);
	// print output
	printf("\nThe accepted jobs in SPT order:\n");
	for (int i = 0; i < jobNum; i++) {
		if (jobArr[i][0] != 0 && jobArr[i][1] != 0) { // don't print 0s
			printf("%d %d\n", jobArr[i][0], jobArr[i][1]);
		}
	}
	printf("\n total completion time = %d\n total rejection cost = %d\n objective = %d", completionTime, rejectCost, objective);
}
