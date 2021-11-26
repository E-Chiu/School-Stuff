#define BUFFER_SIZE 4 // T100 is 4 chars
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
	FILE * logFile;

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
	char currJob[BUFFER_SIZE];
	while(fgets(currJob, BUFFER_SIZE, stdin) != NULL) { // loop until EOF
		if (strchr(currJob, 'S')) { // if you are to sleep then sleep
			memmove(currJob, currJob + 1, strlen(currJob)); // remove first character
			int n = getInt(currJob); // get int from string
			Sleep(n); // call sleep function
		} else if(strchr(currJob, 'T')) { // if trans job send to server
			// send the job
			if( send(sock , currJob , strlen(currJob) , 0) < 0)
			{
				//puts("Send failed");
				return 1;
			}
			
			//Receive a reply from the server
			if( recv(sock , server_reply , 2000 , 0) < 0)
			{
				//puts("recv failed");
				break;
			}
			
			//puts("Server reply :");
			//puts(server_reply);
		}
	}
	
	close(sock);
	return 0;
}