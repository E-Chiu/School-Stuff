/*
cmput 201 l8q1
Date Oct 21, 2020
Refrences: lecture slides, devdocs.io/c, stackoverflow
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#define MAX 101

int main() {
   srand(time(NULL));
   int len = 11; // # of things
   char *thingsArr[len];
   char *temp = malloc(MAX);
   for (int i = 0; i < len; i++) { // get input
      fgets(temp, MAX, stdin);
      thingsArr[i] = malloc(strlen(temp) + 1); // allocate space in array
      strcpy(thingsArr[i], temp); // copy over
   }
   /*
   int testArr[11] = {0,0,0,0,0,0,0,0,0,0,0};
   for (int i = 0; i < 99999; i++) {
      int randInd = rand() % len;
      testArr[randInd] += 1;
   }
   for (int i = 0; i < 11; i++) {
      printf("number %d: %d\n", i + 1, testArr[i]);
   }
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   I used this code and ran it a few times and didn't really
   notice any significant outliers in the numbers so I don't
   really think there was any significant bias in selecting a thing.
   */

   char c;
   while ((c = getchar()) != EOF) { // loop until EOF
      if (c == 10) { // only print if return key
         int randInd = rand() % len; // get random index
         printf("%s", thingsArr[randInd]); // print word
      }
   }
   return 0;
}
