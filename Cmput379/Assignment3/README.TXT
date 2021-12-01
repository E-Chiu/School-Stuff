README FOR ASSIGNMENT3
STUDENT:echiu

INCLUDED FILES:
server.c: server file that makes a server process and listens for messages on a given port

client.c: client file that makes a client process and sends messages on a  given port and ip

functions.c: 2 functions that both client.c and server.c used

tands.c: file that was given to us to use for assignment 2/3

header.h: header file

Makefile: the makefile that makes the executables client and server as well as makes the respective pdf man pages

ASSUMPTIONS:
The main assumption I took in this assignment was how big the buffers should be when reading in strings,
used the BUFFER_SIZE definition very often in this assignment, and it should be big enough to cover most inputs

APPROACH:
I used the example from binarytides.com and modified it to be able to take messages from multiple clients using
select()

HOW TO COMPILE AND RUN:
Calling make should make the files as per the specifications. From there you can execute server by calling 
./server [portNum], and then call client with ./client [port number] [IP address] <[file input]. If you are 
permission denied when trying to run either of the files call "chmod +x ./server" and "chmod +x ./client" to 
fix the problem.