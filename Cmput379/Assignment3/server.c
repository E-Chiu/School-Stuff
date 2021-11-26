/*
	C socket server example taken from binarytides.com
*/

#include<stdio.h>
#include<string.h>	//strlen
#include<sys/socket.h>
#include<arpa/inet.h>	//inet_addr
#include<unistd.h>	//write
#include<stdlib.h>

int main(int argc , char *argv[])
{
	int transactionNum = 1;
	int portNum = atoi(argv[1]); // get portnum from command line

	// ensure port number is in the correct range
	if (portNum < 5000 || portNum > 64000) {
		printf("Port Number out of Range!");
		exit(0);
	}

	FILE * logFile;

	int socket_desc , client_sock , c , read_size;
	struct sockaddr_in server , client;
	char client_message[2000];
	
	//Create socket
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
	{
		printf("Could not create socket");
	}
	puts("Socket created");
	
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
	puts("bind done");
	
	//Listen
	listen(socket_desc , 3);
	
	//Accept and incoming connection
	puts("Waiting for incoming connections...");
	c = sizeof(struct sockaddr_in);
	
	//accept connection from an incoming client
	client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);
	if (client_sock < 0)
	{
		perror("accept failed");
		return 1;
	}
	puts("Connection accepted");
	
	//Receive a message from client
	while( (read_size = recv(client_sock , client_message , 2000 , 0)) > 0 )
	{
		//Send the message back to client
		write(client_sock , client_message , strlen(client_message));
	}
	
	if(read_size == 0)
	{
		puts("Client disconnected");
		fflush(stdout);
	}
	else if(read_size == -1)
	{
		perror("recv failed");
	}
	
	return 0;
}

/*
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
*/