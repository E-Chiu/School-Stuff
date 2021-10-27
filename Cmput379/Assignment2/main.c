#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>
#include "header.h"

// main c file, handling of the inputs will be done here

// initialize global variables for semaphore
queueHead = -1;
ueueTail = -1;
queueSize;
threadID = 1; // starts at one since parent is 0

// intialize other global variables
done = 0; // variable to notify when all jobs are recieved

int main(int argc, char *argv[]) {
    startTime = clock(); // get start time
    // ensure arguments were given
    if (argc == 1) {
        printf("No input was given");
        exit(0);
    }
    // declare all variables from the arguments
    // semaphore not needed as this is before creation of threads
    int threadNum = atoi(argv[1]); // number of threads requested by system
    maxSize =  threadNum * 2;
    jobsQueue = (int*)malloc(sizeof(int) * maxSize); // initialize array big enough to hold consumers
    // if id is given then set id otherwise set as 0
    if (argc == 3) { // open log with specific number
        char logID[JOB_SIZE];
        strcpy(logID, argv[2]); // assume number wont be too big for log size
        char toOpen[STRING_BUFFER];
        strcpy(toOpen, "./prodcon");
        strcat(toOpen, logID);
        strcat(toOpen, ".log");
        logFile = fopen(toOpen, "w");
    } else { // open normal log file
        logFile = fopen("./prodcon.log", "w");
    }
    summary.Thread = (int*)malloc(sizeof(int) * threadNum); // have array for thread summary
    pthread_t threadTid[threadNum]; // array to store thread tids
    if(sem_init(&mutex, 0, 1) < 0) {  // initialize semaphore
        printf("semaphore initialization failed");
    }
    createThreads(threadNum, threadTid); // make requested amount of threads
    char currJob[JOB_SIZE];
    while(fgets(currJob, JOB_SIZE, stdin) != NULL) {
        if (strchr(currJob, 'S')) { // if you are to sleep then sleep
                memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
                int n = getInt(currJob);
                sem_wait(&mutex);
                summary.Sleep += 1;
                sem_post(&mutex);
                Sleep(n); // call sleep function
                printf("\n   %0.3f ID= 0      Sleep %5d", getTime(), n); // print that parent is sleeping
            } else if(strchr(currJob, 'T')) { // if new trans job
                if (getQueueSize() == threadNum * 2) { // if queue is full then wait for spot to be free
                    waitForSpot(threadNum);
                }
                memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
                int n = getInt(currJob);
                sem_wait(&mutex); // wait to enter cs
                if (queueHead == -1) { // if queue is empty reassign head
                    queueHead = 0;
                }
                queueTail = (queueTail + 1) % maxSize; // increment tail
                jobsQueue[queueTail] = n; // add number to array
                queueSize++; // increment queue size
                summary.Ask += 1;
                printf("\n   %0.3f ID= 0 Q= %d Work %6d", getTime(), queueSize, n); // print that parent recieved new job
                sem_post(&mutex); // exit cs
            }
    }
    done = 1; // notify threads that all tasks have been given
    closeThreads(threadNum, threadTid); // close all the threads
    printSummary(threadNum); // print out summary
    fclose(logFile); // close log file
    // free malloced data
    free(jobsQueue);
    free(summary.Thread);
}