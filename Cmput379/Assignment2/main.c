#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>
#include "tands.c"

// main c file, handling of the inputs will be done here

#define JOB_SIZE 4 // T100 4 chars
#define STRING_BUFFER 100 // character buffer since i am unsure how big characters will be

struct Summary {
    int Work;
    int Ask;
    int Recieve;
    int Complete;
    int Sleep;
    int *Thread;
};


// THESE VARIABLES ARE TO BE ACCESSED ONLY THROUGH SEMAPHORES
sem_t mutex;
time_t currTime;
int *jobsQueue;
int queueSize;
int threadID = 0;

struct Summary summary; // make summary struct
FILE *logFile;

// variable to notify when all jobs are recieved
int done = 0;

void *threadStart(void *vargp) { // thread starts and waits for a job, sending status messages to be printed
    int n;
    int ID;
    sem_wait(&mutex);
    ID = threadID; // get the id of this thread and increment it for the next thread
    threadID++;
    sem_post(&mutex);
    printf("ID= %d      Ask", ID); // print that this thread is asking for work
    while (!done) { // infinetley run until last argument has been recieved
        sem_wait(&mutex); // wait for turn to enter cs
        if (queueSize > 0) { // check if there are any jobs in queue
            n = jobsQueue[queueSize]; // get n of current task
            printf("ID= %d Q= %d Recieve    %d", ID, queueSize, n); // announce you are doing the job
            queueSize--; // decrement queue size
            summary.Work += 1;
            sem_post(&mutex);

            Trans(n); // run trans function
            printf("ID= %d      Complete   %d", ID, n); // print that this thread is done working
            printf("ID= %d      Ask", ID); // print that this thread is asking for work
        } else { // otherwise do nothing and free semaphore
            sem_post(&mutex);
        }
    }
    pthread_exit(NULL); // close thread
}

void createThreads(int threadNum, pthread_t *threadTid) { // function creates threadNum number of threads
    for (int i = 0; i < threadNum; i++) {
        pthread_create(&threadTid[i], NULL, threadStart, NULL);
    }
}

void closeThreads(int threadNum, pthread_t *threadTid) { // function waits for all threads to close before returning
    for (int i = 0; i < threadNum; i++) {
        pthread_join(threadTid[i], NULL);
    }
}

int getQueueSize() { // returns current size of the queue
    // enter cs to get size of queue
    int size;
    sem_wait(&mutex);
    size = queueSize;
    sem_post(&mutex);
    return size;
}

void waitForSpot(int threadNum) { // function loops until the queue has room for commands
    while (getQueueSize() == threadNum * 2); // wait for spot to be free
    return;
}

int getInt(char string[JOB_SIZE]) { // function gets number from currjob
    strncpy(string, string, JOB_SIZE - 1); // remove job type
    string[JOB_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc, char *argv[]) {
    // ensure arguments were given
    if (argc == 1) {
        printf("No input was given");
        exit(0);
    }
    // declare all variables from the arguments
    // semaphore not needed as this is before creation of threads
    int threadNum = atoi(argv[1]); // number of threads requested by system
    jobsQueue = (int*)malloc(sizeof(int) * (threadNum * 2)); // initialize array big enough to hold consumers
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
    createThreads(threadNum, threadTid); // make requested amount of threads
    char currJob[JOB_SIZE];
    fgets(currJob, JOB_SIZE, stdin); // get next task
    while(feof(stdin)) {
        if (strchr(currJob, 'S')) { // if you are to sleep then sleep
                int n = getInt(currJob);
                sem_wait(&mutex);
                summary.Sleep += 1;
                sem_post(&mutex);
                Sleep(n); // call sleep function
            } else if(strchr(currJob, 'T')) { // if new trans job
                if (getQueueSize() == threadNum * 2) {
                    // if queue is full then wait for spot to be free
                    waitForSpot(threadNum);
                }
                int n = getInt(currJob);
                sem_wait(&mutex); // wait to enter cs
                jobsQueue[queueSize] = n; // add number to array
                queueSize++; // increment queue size
                summary.Ask += 1;
                sem_post(&mutex); // exit cs
            }
    }
    done = 1; // notify threads that all tasks have been given
    closeThreads(threadNum, threadTid); // close all the threads
}