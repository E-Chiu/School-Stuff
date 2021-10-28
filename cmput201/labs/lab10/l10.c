/*
cmput 201 lab10
Date: Nov 9, 2020
Refrences: devdocs.io/c/
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

void opFloat(char* op, char* str1, char* str2) {
   float num1, num2, result;
   num1 = atof(str1);
   num2 = atof(str2);
   // based on what operation it is do the correct operation and print
   if (!strcmp(op, "add")) {
      result = num1 + num2;
      printf("addition for %s, %s is %f", str1, str2, result);
   } else if(!strcmp(op, "sub")) {
      result = num1 - num2;
      printf("subtraction for %s, %s is %f", str1, str2, result);
   } else if(!strcmp(op, "mul")) {
      result = num1 * num2;
      printf("multiplication for %s, %s is %f", str1, str2, result);
   } else if(!strcmp(op, "div")) {
      if (num2 == 0) { // cannot divide by 0
         printf("division cannot be performed for %s, %s", str1, str2);
      } else {
         result = num1 / num2;
         printf("division for %s, %s is %f", str1, str2, result);
      }
   } else if(!strcmp(op, "mod")) {
      // cannot mod floats
      printf("modulo cannot be performed for %s, %s", str1, str2);
   } else if(!strcmp(op, "pow")) {
      result = powf(num1, num2);
      printf("power for %s, %s is %f", str1, str2, result);
   } else if(!strcmp(op, "log")) {
      result = logf(num2) / logf(num1);
      printf("logarithm for %s, %s is %f", str1, str2, result);
   }
   printf("\n");
}

void opInt(char* op, char* str1, char* str2) {
   int num1, num2, result;
   num1 = atoi(str1);
   num2 = atoi(str2);
   if (!strcmp(op, "add")) {
      result = num1 + num2;
      printf("addition for %s, %s is %d", str1, str2, result);
   } else if(!strcmp(op, "sub")) {
      result = num1 - num2;
      printf("subtraction for %s, %s is %d", str1, str2, result);
   } else if(!strcmp(op, "mul")) {
      result = num1 * num2;
      printf("multiplication for %s, %s is %d", str1, str2, result);
   } else if(!strcmp(op, "div")) {
      if (num2 == 0) { // cannot divide by 0
         printf("division cannot be performed for %s, %s", str1, str2);
      } else {
         result = num1 / num2;
         printf("division for %s, %s is %d", str1, str2, result);
      }
   }  else if(!strcmp(op, "mod")) {
      result = num1 % num2;
      printf("modulo for %s, %s is %d", str1, str2, result);
   } else if(!strcmp(op, "pow")) { // since pow is done with floats must cast
      float result1;
      result1 = powf((float) num1, (float) num2);
      printf("power for %s, %s is %f", str1, str2, result1);
   } else if(!strcmp(op, "log")) { // since log is done with floats must cast
      float result1;
      result1 = logf((float) num2) / logf((float) num1);
      printf("logarithm for %s, %s is %f", str1, str2, result1);
   }
   printf("\n");
}

int main(int argc, char *argv[]) {
   int isFloat = 0;
   if (argc != 4) { // ensure right amount of arguments
      printf("Usage: %s [add|sub|mul|div|mod|pow|log Num Num]", argv[0]);
      exit(0);
   }
   // check if either of the numbers are floats and make sure only digits, - and . are allowed
   int ascii;
   for (char *p = argv[2]; *p != '\0'; p++) {
      if (*p == '.') {
         isFloat = 1;
      }
      ascii = (int) *p;
      if ((ascii != 46 && ascii != 45) && (ascii < 48 || ascii > 57)) { // char must be . - or 0-9
         printf("Usage: %s [add|sub|mul|div|mod|pow|log Num Num]", argv[0]);
         exit(0);
      }
   }
   for (char *p = argv[3]; *p != '\0'; p++) {
      if (*p == '.') {
         isFloat = 1;
      }
      ascii = (int) *p;
      if ((ascii != 46 && ascii != 45) && (ascii < 48 || ascii > 57)) {
         printf("Usage %s [add|sub|mul|div|mod|pow|log Num Num]", argv[0]);
         exit(0);
      }
   }
   if (isFloat) { // do operations based off whether it is a float or not
      opFloat(argv[1], argv[2], argv[3]);
   } else {
      opInt(argv[1], argv[2], argv[3]);
   }
}
