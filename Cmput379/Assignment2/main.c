#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>
#include "header.h"

// main c file, handling of the inputs will be done here

#define JOB_SIZE 4 // T100 4 chars
#define STRING_BUFFER 100 // character buffer since i am unsure how big characters will be

// struct to hold the final stats
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
int *jobsQueue;
int queueHead = -1;
int queueTail = -1;
int queueSize;
int threadID = 1; // starts at one since parent is 0

// general global variables
struct Summary summary; // make summary struct
FILE *logFile; // open file for output
int maxSize; // maximum size of the array

// variable to notify when all jobs are recieved
int done = 0;

int getTime() { // gets time
    time_t currTime = time(NULL);
    int time = (int) currTime;
}

void *threadStart(void *vargp) { // thread starts and waits for a job, sending status messages to be printed
    int n;
    int ID;

    sem_wait(&mutex);
    ID = threadID; // get the id of this thread and increment it for the next thread
    threadID++;
    printf("\n%d ID= %d      Ask", getTime(), ID); // print that this thread is asking for work
    summary.Ask += 1;
    sem_post(&mutex);

    while (!done) { // infiniteley run until last argument has been recieved
        sem_wait(&mutex); // wait for turn to enter cs
        if (queueSize > 0) { // check if there are any jobs in queue
            n = jobsQueue[queueHead]; // get n of current task
            if (queueHead == queueTail) { // if queue is empty reset indexes
                queueHead = -1;
                queueTail = -1;
            } else { // otherwise move head forward normally
                queueHead == (queueHead + 1) % maxSize;
            }
            printf("\n%d ID= %d Q= %d Recieve    %d", getTime(), ID, queueSize, n); // announce you are doing the job
            summary.Recieve += 1;
            queueSize--; // decrement queue size
            summary.Work += 1;
            sem_post(&mutex);

            Trans(n); // run trans function
            printf("\n%d ID= %d      Complete   %d", getTime(), ID, n); // print that this thread is done working
            printf("\n%d ID= %d      Ask", getTime(), ID); // print that this thread is asking for work
            fflush(stdout); // flush stdout just in case
            sem_wait(&mutex);
            summary.Complete += 1;
            summary.Ask += 1;
            sem_post(&mutex);
        } else { // otherwise do nothing and free semaphore
            sem_post(&mutex);
        }
    }
    printf("\nthread exited");
    pthread_exit(NULL); // close thread
}

void createThreads(int threadNum, pthread_t *threadTid) { // function creates threadNum number of threads
    for (int i = 0; i < threadNum; i++) {
        pthread_create(&threadTid[i], NULL, threadStart, NULL);
    }
}

void closeThreads(int threadNum, pthread_t *threadTid) { // function waits for all threads to close before returning
    for (int i = 0; i < threadNum; i++) {
        printf("\nwaiting on thread %d", i);
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
    printf("\n queue free");
    return;
}

int getInt(char string[JOB_SIZE]) { // function gets number from currjob
    strncpy(string, string, JOB_SIZE - 1); // remove job type
    string[JOB_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int printSummary(int threadNum) { // function prints out all the properties of the summary struct
    printf("\nSummary:\nWork: %d\nAsk: %d\nRecieve: %d\nComplete: %d\nSleep: %d\n", summary.Work, summary.Ask, summary.Recieve, summary.Complete, summary.Sleep); // print out summary
    for (int i = 0; i < threadNum; i++) { // loop and print out # of jobs done per thread
        printf("Thread%d: %d", i, summary.Thread[i]);
    }
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
        // logFile = fopen(toOpen, "w");
    } else { // open normal log file
        // logFile = fopen("./prodcon.log", "w");
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
                printf("\n%d ID= 0      Sleep    %d", getTime(), n); // print that parent is sleeping
            } else if(strchr(currJob, 'T')) { // if new trans job
                if (getQueueSize() == threadNum * 2) { // if queue is full then wait for spot to be free
                    printf("\n queue full");
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
                printf("\n%d ID= 0 Q= %d Work    %d", getTime(), queueSize, n); // print that parent recieved new job
                sem_post(&mutex); // exit cs
            }
    }
    printf("\nexited");
    done = 1; // notify threads that all tasks have been given
    printSummary(threadNum); // print out summary
    //fclose(logFile); // close log file
    closeThreads(threadNum, threadTid); // close all the threads
    // free malloced data
    free(jobsQueue);
    free(summary.Thread);
}