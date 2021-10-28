/*
cmput 201 l7q2
Date: Oct 19, 2020
Refrences: none
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

int helper(int *smallest, int len, int arr[len]) {
   // finds the index order of the values
   int index;
   int original = *smallest; // the smallest number from the last call
   for (int i = 0; i < len; i++) {
      if (arr[i] > *smallest && arr[i] != *smallest) { // find the first value > smallest
         *smallest = arr[i];
         index = i;
         for (int j = 0; j < len; j++) {
            if (arr[j] > original && arr[j] < *smallest) { // find number smaller than that
               *smallest = arr[j];
               index = j;
            }
         }
         break; // exit loop
      }
   }
   return index;
}

int main() {
   int len, index;
   int smallest = -1;
   printf("Enter the length of the array: ");
   scanf("%d", &len);
   int arr[len];
   printf("Enter %d distinct positive integers: ", len);
   for (int i = 0; i < len; i++) {
      scanf("%d", &arr[i]);
   }
   printf("Index order: ");
   for (int i = 0; i < len; i++) {
      index = helper(&smallest, len, arr);
      printf("%d, ", index);
   }
}
