/*
cmput 201 l7q3
Date: Oct 19, 2020
Refrences: devdocs.io/c/numeric/math/pow
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <math.h>

int coeffecient(int integer, int size, int coeffArr[999999]) {
   coeffArr[0] += 1; // add 1 to the first coeeffecient
   for (int i = 0; i < size; i++) { // if value is 1 set to -1 and increase next one
      if (coeffArr[i] > 1) {
         coeffArr[i] = -1;
         coeffArr[i + 1] += 1;
         if (i == size - 1) { // if end reached add to size
            size += 1;
            i++;
         }
      }
   }
   // now that coeffecients have been incremented see if answer has been found
   int sum = 0;
   for (int i = 0; i < size; i++) { // calculate sum
      sum += coeffArr[i] * pow(3, i);
   }
   if (sum == integer) {
      return size; // return size if answer found
   }
   return coeffecient(integer, size, coeffArr); // otherwise keep trying to find
}

int main() {
   int integer;
   printf("Enter a positive integer: ");
   scanf("%d", &integer);
   int coeffArr[999999];
   int size = coeffecient(integer, 1, coeffArr);
   printf("Coeffecient sequence: %d", coeffArr[0]);
   for (int *p = &coeffArr[1]; p < &coeffArr[size]; p++) {
      printf(", %d", *p);
   }
   printf("\n");
}
