/*
cmput201 l11q1
Date: Nov 21
Refrences: devdocs.io/c/ on how to use strcat and sprintf
Lab Section: D01
Name: Ethan Chiu
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
   FILE *toRead, *toWrite;
   unsigned int outputNum;
   if(argc != 2) { // ensure correct amount of arguments
      printf("Usage: %s input.txt", argv[0]);
      exit(0);
   }
   printf("Enter the number of output files: ");
   scanf("%d", &outputNum);
   toRead = fopen(argv[1], "r"); // open file to read
   char fileContents[9999][1000];
   int counter = 0;
   while(fgets(fileContents[counter], 1000, toRead) != NULL) { // add lines while not EOF
      fileContents[counter][strlen(fileContents[counter]) - 1] = '\0'; // add null at the end
      counter++;
   }
   fclose(toRead); // close file
   char currentFile[12 + (outputNum % 10)]; // make size of array = to length of "output.txt" + digits in outputNum
   char output[6] = "output";
   char txt[4] = ".txt";
   char numStr[1 + (outputNum % 10)];
   for (int i = 0; i < outputNum; i++) {
      strcpy(currentFile, output);
      sprintf(numStr, "%03d", i);
      strcat(currentFile, numStr); 
      strcat(currentFile, txt);	// concatenate file name
      toWrite = fopen(currentFile, "w"); // open output file
      for (int j = 0; j < counter; j++) {
         fputs(fileContents[j], toWrite); // print contents
      }
      fclose(toWrite);
   }
}
