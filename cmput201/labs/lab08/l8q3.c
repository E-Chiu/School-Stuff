/*
cmput 201 l8q3
Date: Oct 26, 2020
Refrences: geeksforgeeks, stackoverflow "what is uint32_t"
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main() {
   float toMult;
   printf("Enter a floating-point number: ");
   scanf("%f", &toMult);
   uint32_t* bRep = (uint32_t*)(&toMult); // float in binary representation
   uint32_t mask = 0x00800000;
   *bRep = *bRep ^ mask; // xor the first bit before entering loop
   for (int i = 0; i < 8; i++) { 
      if (!(*bRep & mask)) { // see if bit x is not 1
         break;
      }
      mask = mask << 1; // try next bit
      *bRep = *bRep ^ mask;
      if (mask == 0x80000000) { // if still cant add at last exp bit overflow error
         printf("overflow error");
         exit(0);
      }
   }
   printf("Doubling becomes %f", toMult);
}
