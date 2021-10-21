#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>


// main c file, handling of the inputs will be done here

#define JOB_SIZE 4 // T100 4 chars

// THESE VARIABLES ARE TO BE ACCESSED ONLY THROUGH SEMAPHORES
sem_t mutex;
time_h time = time();
int jobsQueue[];
int queueSize;

// variable to notify when all jobs are recieved
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
        sem_wait(&mutex); // wait for turn to enter cs
        if (queueSize > 0) { // check if there are any jobs in queue

        }
        sem_post(&mutex);
    }
    pthread_exit(NULL); // close thread
}

int getInt(char string[JOB_SIZE]) { // get number from currjob
    strcpy(string, &string, JOB_SIZE - 1); // remove job type
    string[JOB_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc, char **argv) {
    // ensure arguments were given
    if (argc == 1) {
        printf("No input was given");
        exit();
    }
    jobsQueue[argv[1] * 2] // initialize array big enough to hold consumers
    int threadNum = argv[1]; // number of threads requested by system
    int programID = 0; // id that should be on the logs
    // if id is given then set id otherwise set as 0
    if (argc == 3) {
        programID = argv[2];
    }
    createThreads(threadNum); // make requested amount of threads
    char currJob[JOB_SIZE];
    fgets(currJob, JOB_SIZE, stdin); // get next task
    while(currJob != EOF) {
        if (strchr(currJob, "S")) { // if you are to sleep then sleep
                int n = getInt(currJob);
                Sleep(n); // call sleep function
            } else if(strchr(currJob, "T")) { // if new trans job
                if ((sizeof(jobsQueue)/sizeof(jobsQueue[0])) == threadNum * 2) {
                    // if queue is full then wait for spot to be free
                    waitForSpot(jobsQueue);
                }
                int n = getInt(currJob);
                sem_wait(&mutex); // wait to enter cs
                jobsQueue[queueSize] = n; // add number to array
                queueSize++;
                sem_post(&mutex); // exit cs
                

            }
    }
    for (int i = 0; i < threadNum; i++) {
        char currJob;

    }
}