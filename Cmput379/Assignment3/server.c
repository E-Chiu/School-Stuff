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

struct client
{
	int transactions;
	int pid;
	char* machineName;
};

void incrementClientTransaction(char *fullname, int clientPid, struct client clientList[MAX_CLIENT], int *numClients) { // check if pid already exists in array, if yes find and increment counter, otherwise make new index
	for (int i = 0; i < *numClients; i++) {
		if (clientList[i].pid == clientPid) { // if pid matches one thats already in array increment counter and leave
			clientList[i].transactions++;
			return;
		}
	}
	
	// reaching here means that it was not added to existing index so new one must be made and incrememnted

	clientList[*numClients].pid = clientPid;
	strcpy(clientList[*numClients].machineName, fullname);
	clientList[*numClients].transactions = 1;
	*numClients++;
	return;
}

int getInt(char string[BUFFER_SIZE]) { // function gets number from currjob
    strncpy(string, string, BUFFER_SIZE - 1); // remove job type
    string[BUFFER_SIZE - 1] = '\0'; // re-append \0
    int n = atoi(string);
    return n;
}

int main(int argc , char *argv[])
{
	float startTime = time(NULL); // to time how long the program runs
	int transactionNum = 0;
	int portNum = atoi(argv[1]); // get portnum from command line
	int numClients = 0; // number of clients
	struct client clientList[MAX_CLIENT]; // array of clients and the transactions each have

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

	fprintf(logFile, "Using port %d\n", portNum); // state what port being

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
	
	//Listen
	listen(socket_desc , 3);
	
	//Accept and incoming connection
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
	timeout.tv_usec = 0;

	fd_set readfds;

	FD_ZERO(&readfds);
	FD_SET(socket_desc, &readfds);
	
	struct sockaddr_in client_address;
	socklen_t lenClient;
	int client_fd;

	while (1) { // loop indefinetley

        lenClient= sizeof(client_address); 

		if (select(socket_desc+1, &readfds, NULL, NULL, &timeout)) { // wait for client to send data
				
				int client_fd = accept(socket_desc, (struct sockaddr*) &client_address, &lenClient); // accept connection

				recv(client_fd , clientJob , 2000 , 0); // recieve message

				char* token = strtok(clientJob, "h"); // get n from the message
				int n = atoi(token); // get int from string
				token = strtok(NULL, "h"); // get name from message
				char * fullName = token; // save name
				token = strtok(NULL, ".");
				token = strtok(NULL, "."); // get pid
				int clientPid = atoi(token); // get pid from string
				incrementClientTransaction(fullName, clientPid, clientList, &numClients); // increment counter

				Trans(n); // call trans function

				// Once done tell the client that it is done
				transactionNum++; // increment transactions
				char doneMsg[BUFFER_SIZE]; 
				sprintf(doneMsg, "%d", transactionNum); // add transaction number
				// send "reciept" back to client
				write(client_fd , doneMsg , strlen(doneMsg));
				printf("reciept sent");
		} else { // if timeout it means server has to close
			float endTime = time(NULL); // get endtime of program
			fprintf(logFile, "\nSUMMARY\n");
			for (int i = 0; i < numClients; i++) { // loop through clients printing their stats
				fprintf(logFile, "   %d Transactions from %s\n", clientList[i].transactions, clientList[i].machineName);
			}
			float totalTime = endTime - startTime;
			float TperS = transactionNum/totalTime;
			fprintf(logFile, "%f transactions/sec (%d/%f)", TperS, transactionNum, totalTime);
			
			// close everything and exit
			close(socket_desc);
			close(client_sock);
			fclose(logFile);
			exit(0);
		}
	}
}