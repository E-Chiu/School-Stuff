#define IP_ADDR_SIZE 15 // ip address is 15 chars

/*
	C ECHO client example using sockets taken from binarytides.com
*/
#include <time.h>
#include <stdio.h>	//printf
#include <string.h>	//strlen
#include <sys/socket.h>	//socket
#include <arpa/inet.h>	//inet_addr
#include <unistd.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include "header.h"

int getInt(char string[BUFFER_SIZE]) { // function gets number from currjob
    strncpy(string, string, BUFFER_SIZE - 1); // remove job type
    string[BUFFER_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc , char *argv[])
{

    int portNum = atoi(argv[1]); // get portnum from command line

	// ensure port number is in the correct range
	if (portNum < 5000 || portNum > 64000) {
		printf("Port Number out of Range!");
		exit(0);
	}

    char ipAddr[IP_ADDR_SIZE];
	strcpy(ipAddr, argv[2]); // get ip address

	// open the log file to write to
	FILE * logFile;

	char hostname[HOST_NAME_MAX + 1];
	gethostname(hostname, HOST_NAME_MAX + 1); // get name of machine

	int pid = getpid();
	// malloc room for pid as string
	char * mypid = malloc(6);
	sprintf(mypid, "%d", pid); // get pid as string
	 
	// malloc room for string
	char *toOpen = malloc(sizeof(hostname) + sizeof(".") + sizeof(mypid));

	strcpy(toOpen, hostname);
	strcat(toOpen, ".");
	strcat(toOpen, mypid);

	logFile = fopen(toOpen, "w"); // open logfile in write mode

	// print port, ip addr, and host used to log
	fprintf(logFile, "Using port %d\nUsing server address %s\nHost %s", portNum, ipAddr, toOpen);

	// free malloced variables
	free(toOpen);
	free(mypid); 

	int sock;
	struct sockaddr_in server;
	char message[1000] , server_reply[2000];
	
	//Create socket
	sock = socket(AF_INET , SOCK_STREAM , 0);
	if (sock == -1)
	{
		printf("Could not create socket");
	}
	//puts("Socket created");
	
	server.sin_addr.s_addr = inet_addr(ipAddr); // changed to connect with given ip
	server.sin_family = AF_INET;
	server.sin_port = htons( portNum ); // changed to connect to given port

	//Connect to remote server
	if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0)
	{
		perror("connect failed. Error");
		return 1;
	}
	
	//puts("Connected\n");
	
	//keep communicating with server
	int transactions = 1;
	char currJob[BUFFER_SIZE];
	while(fgets(currJob, BUFFER_SIZE, stdin) != NULL) { // loop until EOF
		transactions++; // increment transactions
		if (strchr(currJob, 'S')) { // if you are to sleep then sleep
			memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
			int n = getInt(currJob); // get int from string
			Sleep(n); // call sleep function
			fprintf(logFile, "Sleep %d units", n); // print that you slept
		} else if(strchr(currJob, 'T')) { // if trans job send to server
			memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
			int n = getInt(currJob); // get int from string
			// send the job
			if( send(sock , currJob , strlen(currJob) , 0) < 0)
			{
				puts("Send failed");
				return 1;
			}

			fprintf(logFile, "%u.2: Send (T %d)", (unsigned) time(NULL), n); // print that trans was sent
			
			//Receive a reply from the server
			if( recv(sock , server_reply , 2000 , 0) < 0)
			{
				puts("recv failed");
				break;
			}
			
			fprintf(logFile, "%u.2: Recv (D %d)", (unsigned) time(NULL), n); // print that "reciept" was recieved
		}
	}
	fprintf(logFile, "Sent %d transactions", transactions); // notify how many transactions were done
	
	close(sock);
	return 0;
}