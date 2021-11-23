#DEFINE BUFFER_SIZE 4 // T100 is 4 chars

#include <stdio.h>
#include <time.h>

char input[BUFFER_SIZE];

int getInt(char string[JOB_SIZE]) { // function gets number from currjob
    strncpy(string, string, JOB_SIZE - 1); // remove job type
    string[JOB_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc , char *argv[]) {
    if (argc == 1) { // get port number
        int portNum = argv[1];
    } else if (argc == 2) { // get port number and ip to run on
        int portNum = argv[1];
        int ipAddr = argv[2];
    }

    while(fgets(currJob, JOB_SIZE, stdin) != NULL) { // loop until EOF is detected
        if (strchr(currJob, 'S')) { // if you are to sleep then sleep
                memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
                int n = getInt(currJob);
                Sleep(n); // call sleep function
            } else if(strchr(currJob, 'T')) { // if new trans job
                int n = getInt(currJob);
                Trans(n);
            }
    }
}