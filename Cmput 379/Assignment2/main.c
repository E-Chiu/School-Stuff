#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

// main c file, handling of the inputs will be done here

int done = 0;

void createThreads(int threadNum) {
    for (int i = 0; i < threadNum; i++) {
        pthread_t pthread_id;
        pthread_create(&pthread_id, NULL, threadStart, NULL);
    }
}

void waitForSpot(int jobsQueue[]) {
    while ((sizeof(jobsQueue)/sizeof(jobsQueue[0])) == threadNum * 2); // wait for spot to be free
    return;
}

void *threadStart(void *vargp) { // thread starts and waits for a job, sending status messages to be printed
    while (not done) { // infinetley run until last argument has been recieved
        printf("")
    }
    pthread_exit(NULL); // close thread
}

int main(int argc, char **argv) {
    // ensure arguments were given
    if (argc == 1) {
        printf("No input was given");
        exit();
    }
    int jobsQueue[argv[1] * 2] // initialize array big enough to hold consumers
    int threadNum = argv[1]; // number of threads requested by system
    int programID = 0; // id that should be on the logs
    time_h time = time();
    // if id is given then set id otherwise set as 0
    if (argc == 3) {
        programID = argv[2];
    }
    createThreads(threadNum);
    char currJob[4]; // T100 is 4 digits
    fgets(currJob, 4, stdin); // get next task
    while(currJob != EOF) {
        if ((sizeof(jobsQueue)/sizeof(jobsQueue[0])) == threadNum * 2) { // if queue is full then wait for spot to be free
            waitForSpot(jobsQueue);
        }
        
    }
    for (int i = 0; i < threadNum; i++) {
        char currJob;

    }
}