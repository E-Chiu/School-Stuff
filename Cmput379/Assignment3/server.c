/*
	C socket server example taken from binarytides.com
*/

#include <stdio.h>
#include <string.h>	//strlen
#include <sys/socket.h>
#include <arpa/inet.h>	//inet_addr
#include <unistd.h>	//write
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <limits.h>
#include "header.h"

int getInt(char string[BUFFER_SIZE]) { // function gets number from currjob
    strncpy(string, string, BUFFER_SIZE - 1); // remove job type
    string[BUFFER_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc , char *argv[])
{
	int transactionNum = 1;
	int portNum = atoi(argv[1]); // get portnum from command line

	// ensure port number is in the correct range
	if (portNum < 5000 || portNum > 64000) {
		printf("Port Number out of Range!");
		exit(0);
	}

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

	// free malloced variables
	free(toOpen);
	free(mypid); 

	fprintf(logFile, "Using port %d", portNum); // state what port being

	int socket_desc , client_sock , c , read_size;
	struct sockaddr_in server , client;
	char clientJob[2000];
	
	//Create socket
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
	{
		printf("Could not create socket");
	}
	//puts("Socket created");
	
	//Prepare the sockaddr_in structure
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons( portNum ); // changed to use any port number
	
	//Bind
	if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
	{
		//print the error message
		perror("bind failed. Error");
		return 1;
	}
	//puts("bind done");
	
	//Listen
	listen(socket_desc , 3);
	
	//Accept and incoming connection
	//puts("Waiting for incoming connections...");
	c = sizeof(struct sockaddr_in);
	
	//accept connection from an incoming client
	client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);
	if (client_sock < 0)
	{
		perror("accept failed");
		return 1;
	}
	puts("Connection accepted");
	
	// struct to set timeout to be 30s
	struct timeval timeout;
	timeout.tv_sec = 30;
	timeour.tv_usec = 0;

	//Receive a message from client
	while( (read_size = recv(client_sock , clientJob , 2000 , 0)) > 0 )
	{
		memmove(clientJob, clientJob + 1, strlen(clientJob)); // remove first character
		int n = getInt(clientJob); // get int from string
		Trans(n); // call trans function

		//Once done tell the client that it is done
		char doneMsg[] = "D";
		doneMsg[2] = transactionNum; // add transaction number
		transactionNum++; // increment transactions

		// send "reciept" back to client
		write(client_sock , doneMsg , strlen(doneMsg));
	}
	
	if(read_size == 0)
	{
		//puts("Client disconnected");
		fflush(stdout);
	}

	else if(read_size == -1)
	{
		//perror("recv failed");
	}
	
	return 0;
}