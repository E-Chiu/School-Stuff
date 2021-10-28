/*
cmput 201 l6q1
Date Oct 7, 2020
Refrences: None
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#define N 10

int main() {
    int b[N];
    int *a = &b[0];
    int *p = a, *q = a + N - 1;
    for (int i = N-1; i >= 0 ; i--) {
        *(a + i) = i + 1;
    }

    while (p < q) {
        int temp = *p;
        *p++ = *q;
        *q-- = temp;
    }
        
    for (p = &b[0]; p < &b[10]; p++) {
	printf("%d ", *p);
   }
	printf("\n");
  
    return 0;
}
