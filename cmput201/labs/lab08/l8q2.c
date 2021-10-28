/*
cmput 201 l8q2
Date: Oct 23, 2020
Refrences: Code from lab specification
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <stdlib.h>

int findGCD(int i, int j) {
    // code adapted from lab information to find the GCD
    while (i != j) {
        i > j ? (i -= j) : (j -= i); // subtract from values until values are equal
    }
    return i;
}

void findCoeff(int i, int j, int gcd, int* a, int* b, int swapped) {
   if (i > j) { // have the smaller value in i for convenience
      int temp = i;
      i = j;
      j = temp;
      swapped = 1;
   }
   if ((i * *a) + (j * *b) == gcd) { // return when answer is found
      if (swapped) { // if values were swapped swap them back
         int temp = i;
         i = j;
         j = temp;
         temp = *a;
         *a = *b;
         *b = temp;
      }
   } else if ((i * -(*a)) <= (j * *b)) { // if a*i is less than b*j smaller value has to be lower
      *a -= 1;
      findCoeff(i, j, gcd, a, b, swapped);
   } else if ((i * -(*a)) > (j * *b)) { // if a*i is greater than b*j bigger value has to be higher
      *b += 1;
      findCoeff(i, j, gcd, a, b, swapped);
   }
}

int main() {
   int i, j;
   printf("Enter two positive integers: ");
   scanf("%d%d", &i, &j); // get user input
   if(i < 0 || j < 0) {
      exit(0); // exit if value(s) are not positive
   }
   int gcd = findGCD(i, j); // find GCD
   int a = 0, b = 0;
   findCoeff(i, j, gcd, &a, &b, 0); // find coeff
   // print results
   if (a < 0) { // print this one if a is negative
      printf("GCD: %d = (%d) * %d + %d * %d\n", gcd, a, i, b, j);
   } else { // print this one if b is negative
      printf("GCD: %d = %d * %d + (%d) * %d\n", gcd, a, i, b, j); 
   }
   return 0;
}


