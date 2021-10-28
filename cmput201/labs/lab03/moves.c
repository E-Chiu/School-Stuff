#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
int main() {
	int number = 0;
	srand(time(0));
	for (int i = 0; i < 5000; i++) {
	number = rand() % 4 + 1;
	printf("%d ", number); 
	}
}
