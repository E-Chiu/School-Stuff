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
#include <sys/types.h>
#include <netinet/in.h> 
#include <limits.h>
#include "header.h"

struct client
{
	int transactions;
	int pid;
	char machineName[BUFFER_SIZE];
};

int incrementClientTransaction(char *fullname, int clientPid, struct client clientList[MAX_CLIENT], int numClients) { // check if pid already exists in array, if yes find and increment counter, otherwise make new index
	for (int i = 0; i < numClients; i++) {
		if (clientList[i].pid == clientPid) { // if pid matches one thats already in array increment counter and leave
			clientList[i].transactions++;
			return numClients;
		}
	}
	
	// reaching here means that it was not added to existing index so new one must be made and incrememnted

	clientList[numClients].pid = clientPid;
	strcpy(clientList[numClients].machineName, fullname);
	clientList[numClients].transactions = 1;
	numClients++;
	return numClients;
}

int main(int argc , char *argv[])
{
	char startTime[BUFFER_SIZE];
	char storeTime[BUFFER_SIZE]; // used every time to get time
	strcpy(startTime, getTime(startTime)); // to time how long the program runs
	int transactionNum = 0;
	int portNum = atoi(argv[1]); // get portnum from command line
	int numClients = 0; // number of clients
	struct client clientList[MAX_CLIENT]; // array of clients and the transactions each have
	char * useless; // used for strtod

	// ensure port number is in the correct range
	if (portNum < 5000 || portNum > 64000) {
		puts("Port Number out of Range!");
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

	int socket_desc , client_sock[MAX_CLIENT] , read_size;
	struct sockaddr_in server , client;
	char clientJob[2000];
	
	// initialize client sockets
	for (int i = 0 ; i < MAX_CLIENT; i++) {
		client_sock[i] = 0;
	}

	//Create socket
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
	{
		puts("Could not create socket");
	}
	
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
	
	//Listen, only 3 clients max at a time
	if (listen(socket_desc , 3) < 0) {
		puts("listen failed");
	}

	fd_set readfds;

	while (1) { // loop indefinetley

		// struct to set timeout to be 30s
		struct timeval timeout;
		timeout.tv_sec = 30;
		timeout.tv_usec = 0;

		int max_sd, sd;
		
		struct sockaddr_in client_address;
		int lenClient;
		int client_fd;
		lenClient= sizeof(client_address); 

		// reset variables
		FD_ZERO(&readfds);
		FD_SET(socket_desc, &readfds);
		max_sd = socket_desc;

		for (int i = 0; i < MAX_CLIENT; i++) {
			sd = client_sock[i]; // get socket

			if (sd > 0) { // check if sd is open and then add to list
				FD_SET(sd, &readfds);
			}

			if (sd > max_sd) { // get sd max
				max_sd = sd;
			}
		}

		if (select(max_sd+1, &readfds, NULL, NULL, &timeout)) { // wait for client to send message
			if(FD_ISSET(socket_desc, &readfds)) { // get new connection

				if ((client_fd = accept(socket_desc, (struct sockaddr*) &client_address, (socklen_t*)&lenClient)) < 0) { // accept connection
					puts("accept failed");
				}

				// add to list
				for (int i = 0; i < MAX_CLIENT; i++) {
					if(client_sock[i] == 0) {
						client_sock[i] = client_fd;
						break;
					}
				}
			} else { // check existing connections
				for(int i = 0; i < MAX_CLIENT; i++) {
					sd = client_sock[i]; // loop

					if(FD_ISSET(sd, &readfds)) {
						int numb = recv(sd , clientJob , 2000 , 0); // recieve message

						if (numb > 0) {
							transactionNum++; // increment transactions
							char* token = strtok(clientJob, "."); // get n from the message
							int n = atoi(token); // get int from string
							token = strtok(NULL, "."); // get name from message
							char machineName[BUFFER_SIZE];
							strcpy(machineName, token); // save name
							token = strtok(NULL, "."); // get pid
							strcat(machineName, ".");
							strcat(machineName, token);
							int clientPid = atoi(token); // get pid from string
							numClients = incrementClientTransaction(machineName, clientPid, clientList, numClients); // increment counter

							fprintf(logFile, "%s: #%3d (T%3d) from %s\n", getTime(storeTime), transactionNum, n, machineName); // print what you are about to do
							Trans(n); // call trans function
							fprintf(logFile, "%s: #%3d (Done) from %s\n", getTime(storeTime), transactionNum, machineName); // print that you finished

							// Once done tell the client that it is done
							char doneMsg[BUFFER_SIZE]; 
							sprintf(doneMsg, "%d", transactionNum); // add transaction number
							// send "reciept" back to client
							write(sd , doneMsg , strlen(doneMsg));

							memset(clientJob, 0, sizeof(clientJob)); // clean string
						} else if(numb == 0) { // client has shut down
							close(sd); // end the connection
							client_sock[i] = 0; // remove from list
						} else{
							puts("recv failed");
						}
					}
				}
			}
		} else { // if timeout it means server has to close
			char endTime[BUFFER_SIZE];
			strcpy(endTime, getTime(endTime)); // get endtime of program
			fprintf(logFile, "\nSUMMARY\n");
			for (int i = 0; i < numClients; i++) { // loop through clients printing their stats
				fprintf(logFile, "   %d Transactions from %s\n", clientList[i].transactions, clientList[i].machineName);
			}
			float totalTime = strtod(endTime, &useless) - strtod(startTime, &useless);
			float TperS = transactionNum/totalTime;
			fprintf(logFile, "%.1f transactions/sec (%d/%f)", TperS, transactionNum, totalTime);
			
			// close everything and exit
			close(socket_desc);
			for (int i = 0; i < MAX_CLIENT; i++) {
				close(client_sock[i]);
			}
			close(client_fd);
			fclose(logFile);
			exit(0);
		}
	}
}