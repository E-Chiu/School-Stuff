// defines
#define JOB_SIZE 4 // T100 4 chars
#define STRING_BUFFER 100 // character buffer since i am unsure how big characters will be

// THESE VARIABLES ARE TO BE ACCESSED ONLY THROUGH SEMAPHORES
extern sem_t mutex;
extern int *jobsQueue;
extern int queueHead;
extern int queueTail;
extern int queueSize;
extern int threadID;

// other global variables
extern struct Summary summary; // make summary struct
extern FILE *logFile; // open file for output
extern int maxSize;  // maximum size of the array
extern int done;  // variable to notify when all jobs are recieved
extern clock_t startTime; // start time of the program used to 
extern float lastTime; // last time recieved by getTime used to print total transactions

// struct to hold the final stats
struct Summary {
    int Work;
    int Ask;
    int Recieve;
    int Complete;
    int Sleep;
    int *Thread;
};

// prototypes for functions in tands.c

void Trans(int n);

void Sleep(int n);

// for functions.c

float getTime();

void *threadStart(void *vargp);

void createThreads(int threadNum, pthread_t *threadTid);

void closeThreads(int threadNum, pthread_t *threadTid);

int getQueueSize();

void waitForSpot(int threadNum);

int getInt(char string[JOB_SIZE])

int printSummary(int threadNum);