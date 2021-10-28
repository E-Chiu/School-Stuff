/*
Cmput 201 l7q1
Date: Oct 15, 2020
Refrences: Stackoverflow "get nth byte of integer"
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

void byte_value(int *);

int main() {
    int n = 1;
    byte_value(&n);
    
    printf("Enter an integer: ");
    if (scanf("%d", &n) == 1)
        byte_value(&n);
    
    return 0;        
}

void byte_value(int *p) {
    // fill in the body using only pointer variables
    // printout the memory address of the byte and its unsigned char (integer) value
    // one line for each pair, a total of 4 lines
    unsigned char* uchar = (unsigned char*)p;
    for (int i = 0; i < 4; i++) {
       printf("memory address: %p byte: %x\n", uchar + i, (*p >> (8 * i)) & 0xff);
    }
    return;
}
