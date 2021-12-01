#define IP_ADDR_SIZE 15 // ip address is 15 chars

/*
	C ECHO client example using sockets taken from binarytides.com
*/
#include <time.h>
#include <stdio.h>
#include <string.h>	//strlen
#include <sys/socket.h>	//socket
#include <arpa/inet.h>	//inet_addr
#include <unistd.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include "header.h"

int main(int argc , char *argv[])
{
    int portNum = atoi(argv[1]); // get portnum from command line

	// ensure port number is in the correct range
	if (portNum < 5000 || portNum > 64000) {
		puts("Port Number out of Range!");
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
	char * mypid = malloc(PID_SIZE);
	sprintf(mypid, "%d", pid); // get pid as string
	 
	// malloc room for string
	char *toOpen = malloc(sizeof(hostname) + sizeof(".") + sizeof(mypid));

	strcpy(toOpen, hostname);
	strcat(toOpen, ".");
	strcat(toOpen, mypid);

	logFile = fopen(toOpen, "w"); // open logfile in write mode

	// print port, ip addr, and host used to log
	fprintf(logFile, "Using port %d\nUsing server address %s\nHost %s\n", portNum, ipAddr, toOpen);

	int sock;
	struct sockaddr_in server;
	char message[1000] , server_reply[2000];
	
	//Create socket
	sock = socket(AF_INET , SOCK_STREAM , 0);
	if (sock == -1)
	{
		puts("Could not create socket");
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
	int transactions = 0;
	char storeTime[BUFFER_SIZE]; // used to store time
	char currJob[BUFFER_SIZE];
	char seperator[] = ".";
	while(fgets(currJob, BUFFER_SIZE, stdin) != NULL) { // loop until EOF
		currJob[ strcspn(currJob, "\n") ] = '\0'; // remove newline
		if (strchr(currJob, 'S')) { // if you are to sleep then sleep
			memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
			int n = getInt(currJob); // get int from string
			Sleep(n); // call sleep function

			fprintf(logFile, "Sleep %d units\n", n); // print that you slept
		} else if(strchr(currJob, 'T')) { // if trans job send to server
			memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
			int n = getInt(currJob); // get int from string

			// construct name of the current process to be sent to server
			strcat(currJob, seperator); // add h to seperate n and hostname
			strcat(currJob, toOpen); // add the pid to the end of the string

			// send the job
			if( send(sock , currJob , strlen(currJob) , 0) < 0)
			{
				puts("Send failed");
				return 1;
			}

			transactions++; // increment transactions

			fprintf(logFile, "%s: Send (T %d)\n", getTime(storeTime), n); // print that trans was sent
			
			//Receive a reply from the server
			if( recv(sock , server_reply , 2000 , 0) < 0)
			{
				puts("recv failed");
				break;
			}
			int d = atoi(server_reply);
			fprintf(logFile, "%s: Recv (D %d)\n", getTime(storeTime), d); // print that "reciept" was recieved
		}
		memset(currJob, 0, sizeof(currJob)); // clean string
	}
	fprintf(logFile, "Sent %d transactions", transactions); // notify how many transactions were done
	
	// free malloced variables
	free(toOpen);
	free(mypid); 
	// close everything and exit
	fclose(logFile);
	close(sock);
	return 0;
}