CFLAGS=-I -W -O -g.

all: server client

server: server.o tands.o
	gcc -o server server.o tands.o 

client: client.o
	gcc -o client client.o tands.o
	
server.o: server.c
	gcc -c server.c

client.o: client.c
	gcc -c client.c

tands.o: tands.c
	gcc -c tands.c

clean:
	rm *.o server client
