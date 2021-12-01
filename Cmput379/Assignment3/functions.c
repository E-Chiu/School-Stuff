#include <sys/time.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "header.h"

// shared functions between client and server

// given the job string takes away either t/s (the first char)
int getInt(char string[BUFFER_SIZE]) { // function gets number from currjob
    strncpy(string, string, BUFFER_SIZE - 1); // remove job type
    string[BUFFER_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}


// returns the epoch time as a string
char* getTime(char *toStore) {
    struct timeval tv;

    gettimeofday(&tv, 0);

    sprintf(toStore, "%d.%2d", (int)tv.tv_sec, (int)tv.tv_usec/10000);

    return toStore;
}