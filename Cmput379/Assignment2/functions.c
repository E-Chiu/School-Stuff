#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>
#include "header.h"

// declare semaphore variables
sem_t mutex;
int *jobsQueue;
int queueHead;
int queueTail;
int queueSize;
int threadID;

// decalare other global variables
struct Summary summary; // make summary struct
FILE *logFile; // open file for output
int maxSize;  // maximum size of the array
int done;  // variable to notify when all jobs are recieved
clock_t startTime; // start time of the program used to 
float lastTime; // last time recieved by getTime used to print total transactions


// all the functions needed by main.c are declared here

float getTime() { // gets time
    clock_t currTime = clock();
    float time = (float) (currTime - startTime) /  CLOCKS_PER_SEC;
    lastTime = time;
    return time;
}

void *threadStart(void *vargp) { // thread starts and waits for a job, sending status messages to be printed
    int n;
    int ID;

    sem_wait(&mutex);
    ID = threadID; // get the id of this thread and increment it for the next thread
    threadID++;
    fprintf(logFile, "\n   %0.3f ID= %d      Ask", getTime(), ID); // print that this thread is asking for work
    summary.Ask += 1;
    sem_post(&mutex);

    while (!done || queueSize > 0) { // infiniteley run until last argument has been recieved and queue is empty
        sem_wait(&mutex); // wait for turn to enter cs
        if (queueSize > 0) { // check if there are any jobs in queue
            n = jobsQueue[queueHead]; // get n of current task
            if (queueHead == queueTail) { // if queue is empty reset indexes
                queueHead = -1;
                queueTail = -1;
            } else { // otherwise move head forward normally
                queueHead == (queueHead + 1) % maxSize;
            }
            fprintf(logFile, "\n   %0.3f ID= %d Q= %d Recieve %3d", getTime(), ID, queueSize, n); // announce you are doing the job
            summary.Recieve += 1;
            queueSize--; // decrement queue size
            summary.Work += 1;
            summary.Thread[ID - 1]++; // record that the thread did a task
            sem_post(&mutex);

            Trans(n); // run trans function
            fprintf(logFile, "\n   %0.3f ID= %d      Complete %2d", getTime(), ID, n); // print that this thread is done working
            fprintf(logFile, "\n   %0.3f ID= %d      Ask", getTime(), ID); // print that this thread is asking for work
            fflush(stdout); // flush stdout just in case
            sem_wait(&mutex);
            summary.Complete += 1;
            summary.Ask += 1;
            sem_post(&mutex);
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

int printSummary(int threadNum) { // function prints out all the properties of the summary struct
    fflush(stdout);
    fprintf(logFile, "\nSummary:\n   Work: %12d\n   Ask: %13d\n   Recieve: %9d\n   Complete: %8d\n   Sleep: %11d", summary.Work, summary.Ask, summary.Recieve, summary.Complete, summary.Sleep); // print out summary
    for (int i = 0; i < threadNum; i++) { // loop and print out # of jobs done per thread
        fprintf(logFile, "\n   Thread %d: %8d", i + 1, summary.Thread[i]);
    }
    fprintf(logFile, "\nTransactions per second: %2.2f", summary.Work / lastTime);
}
