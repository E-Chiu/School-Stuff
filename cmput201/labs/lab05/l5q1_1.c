/*
cmput 201 l5q1_1
Date: Sept 30, 2020
Refrences: None
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

float calculate_addition(float num_one, float num_two) {
    return num_one + num_two;
}

int main() {
    
    //set up two float variables and interface to accept from user input
    //print the sum of the entered two float numbers
    
    printf("%f", calculate_addition(5, 5));
    return 0;
}
