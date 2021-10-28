/*
cmput 201 l11q2
Date: Nov 21, 2020
Refrences: none
Lab Section: D01
Name: Ethan Chiu
I may have misunderstood lab 8 because i did something similar with bitshifting and masks
*/

#include <stdio.h>
#include <stdint.h>

int main() {
   float input;
   printf("Enter a floating-point number: ");
   scanf("%f", &input);
   uint32_t* hexa = (uint32_t*)(&input); // cast the float to uint32_t to store as hexa
   uint32_t mask = 0x00800000;
   *hexa = *hexa ^ mask;
   for (int i = 0; i < 8; i++) { 
      if (!(*hexa & mask) && mask == 0x80000000) { // if mask goes to max break
         break;
      }
      mask = mask << 1; // shift by one then xor
      *hexa = *hexa ^ mask;
   }
   printf("Doubling becomes %f", input);
}
